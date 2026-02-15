from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
from model.skin_type_cnn import predict_skin_type_simple
from model.recommendation_model import generate_recommendations
from products_database import get_products_by_category, search_products, SKINCARE_PRODUCTS, get_recommended_products, get_top_rated_products
import config

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = config.UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = config.MAX_CONTENT_LENGTH
app.secret_key = config.SECRET_KEY

# Create upload directory if it doesn't exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# MongoDB connection (optional - comment out if not using MongoDB)
try:
    client = MongoClient(config.MONGO_URI)
    db = client.skincare_ai
    # Test connection
    client.admin.command('ping')
    print("MongoDB connected successfully")
except Exception as e:
    print(f"MongoDB connection failed: {e}")
    client = None
    db = None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Step 1: Predict skin type
            try:
                skin_type = predict_skin_type_simple(filepath)
                print(f"Predicted skin type: {skin_type}")
            except FileNotFoundError as e:
                return render_template("index.html", error="Model not found. Please train the model first.")
            except Exception as e:
                return render_template("index.html", error=f"Prediction error: {str(e)}")

            # Step 2: Assume some detected issues (placeholder)
            # In production: integrate with skin issue detection ML model
            detected_issues = ["acne", "dullness"]

            # Step 3: Generate AI-powered product recommendations
            product_recommendations = get_recommended_products(skin_type, detected_issues)
            print(f"Product recommendations count: {len(product_recommendations)}")
            print(f"First product: {product_recommendations[0] if product_recommendations else 'None'}")
            
            # Step 4: Generate comprehensive recommendations
            recommendations = generate_recommendations(skin_type, detected_issues)
            recommendations['products'] = product_recommendations

            # Save in DB (if MongoDB is available)
            if db is not None:
                try:
                    db.users.insert_one({
                        "image": filename,
                        "skin_type": skin_type,
                        "issues": detected_issues,
                        "recommendations": recommendations
                    })
                except Exception as e:
                    print(f"Database save error: {e}")

            # Format recommendations for template
            formatted_recommendations = {
                'products': product_recommendations,
                'routine_steps': recommendations.get('routine_steps', []),
                'tips': recommendations.get('tips', [])
            }
            
            return render_template("result.html", 
                                 image=filename, 
                                 skin_type=skin_type, 
                                 recommendations=formatted_recommendations,
                                 detected_issues=detected_issues)

    return render_template("index.html")

@app.route("/products")
def products():
    """Display all products"""
    category = request.args.get('category', 'all')
    skin_type = request.args.get('skin_type', None)
    
    if category == 'all':
        products = []
        for cat in SKINCARE_PRODUCTS.values():
            if isinstance(cat, list):
                products.extend(cat)
            else:
                for skin_products in cat.values():
                    if isinstance(skin_products, list):
                        products.extend(skin_products)
    else:
        products = get_products_by_category(category, skin_type)
    
    return jsonify(products)

@app.route("/search")
def search():
    """Search products"""
    query = request.args.get('q', '')
    if query:
        results = search_products(query)
        return jsonify(results)
    return jsonify([])

@app.route("/api/skin-types")
def skin_types():
    """Get available skin types"""
    return jsonify(['dry', 'normal', 'oily'])

@app.route("/api/categories")
def categories():
    """Get product categories"""
    return jsonify(list(SKINCARE_PRODUCTS.keys()))

@app.route("/api/products/<int:product_id>")
def get_product(product_id):
    """Get specific product details"""
    from products_database import get_product_by_id
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route("/api/products/top-rated")
def top_rated_products():
    """Get top-rated products"""
    limit = request.args.get('limit', 10, type=int)
    products = get_top_rated_products(limit)
    return jsonify(products)

@app.route("/api/products/price-range")
def products_by_price():
    """Get products by price range"""
    min_price = request.args.get('min', 0, type=float)
    max_price = request.args.get('max', 1000, type=float)
    from products_database import get_products_by_price_range
    products = get_products_by_price_range(min_price, max_price)
    return jsonify(products)

@app.route("/api/recommendations")
def api_recommendations():
    """Get product recommendations via API"""
    skin_type = request.args.get('skin_type', 'normal')
    issues = request.args.getlist('issues')
    
    if skin_type not in ['dry', 'normal', 'oily']:
        return jsonify({"error": "Invalid skin type"}), 400
    
    recommendations = get_recommended_products(skin_type, issues)
    return jsonify(recommendations)

@app.errorhandler(413)
def too_large(e):
    return render_template("index.html", error="File too large. Please upload an image smaller than 16MB."), 413

@app.errorhandler(404)
def not_found(e):
    return render_template("index.html", error="Page not found."), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("index.html", error="Server error. Please try again later."), 500

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
