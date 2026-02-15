"""
Professional Skincare Products Database
Contains comprehensive product information for AI-powered recommendations
"""

# Comprehensive professional skincare products database
SKINCARE_PRODUCTS = {
    "cleanser": {
        "dry": [
            {
                "id": 1,
                "name": "CeraVe Hydrating Foaming Oil Cleanser",
                "brand": "CeraVe",
                "price": 1327.17,
                "rating": 4.5,
                "description": "Gentle foaming cleanser with ceramides and hyaluronic acid for dry skin. Removes makeup and impurities without stripping natural oils.",
                "ingredients": ["Ceramides", "Hyaluronic Acid", "Vitamin B5", "Triglycerides"],
                "image": "cerave-hydrating-cleanser.jpg",
                "category": "cleanser",
                "skin_type": "dry",
                "benefits": ["Hydrating", "Gentle", "Non-stripping", "Makeup removal"],
                "usage": "Apply to wet skin, massage gently, rinse thoroughly. Use morning and evening.",
                "size": "236ml",
                "reviews": 1250
            },
            {
                "id": 2,
                "name": "Neutrogena Ultra Gentle Daily Cleanser",
                "brand": "Neutrogena",
                "price": 746.17,
                "rating": 4.2,
                "description": "Ultra-gentle cleanser for sensitive and dry skin. Dermatologist recommended formula.",
                "ingredients": ["Glycerin", "Mild Surfactants", "Panthenol"],
                "image": "neutrogena-gentle-cleanser.jpg",
                "category": "cleanser",
                "skin_type": "dry",
                "benefits": ["Gentle", "Non-comedogenic", "Fragrance-free", "Hypoallergenic"],
                "usage": "Apply to wet skin, massage gently, rinse with lukewarm water.",
                "size": "354ml",
                "reviews": 890
            },
            {
                "id": 3,
                "name": "Aveeno Ultra-Calming Foaming Cleanser",
                "brand": "Aveeno",
                "price": 621.67,
                "rating": 4.3,
                "description": "Calming cleanser with feverfew extract for sensitive, dry skin.",
                "ingredients": ["Feverfew Extract", "Glycerin", "Oat Kernel Extract"],
                "image": "aveeno-calming-cleanser.jpg",
                "category": "cleanser",
                "skin_type": "dry",
                "benefits": ["Calming", "Sensitive skin", "Natural ingredients"],
                "usage": "Pump into hands, apply to wet face, massage and rinse.",
                "size": "177ml",
                "reviews": 567
            }
        ],
        "normal": [
            {
                "id": 4,
                "name": "Cetaphil Daily Facial Cleanser",
                "brand": "Cetaphil",
                "price": 1078.17,
                "rating": 4.3,
                "description": "Gentle daily cleanser suitable for normal skin. Maintains skin's natural pH balance.",
                "ingredients": ["Glycerin", "Mild Cleansing Agents", "Panthenol"],
                "image": "cetaphil-daily-cleanser.jpg",
                "category": "cleanser",
                "skin_type": "normal",
                "benefits": ["Gentle", "Daily use", "Non-irritating", "pH balanced"],
                "usage": "Apply to wet skin, massage gently, rinse thoroughly.",
                "size": "237ml",
                "reviews": 2100
            },
            {
                "id": 5,
                "name": "Fresh Soy Face Cleanser",
                "brand": "Fresh",
                "price": 3154.0,
                "rating": 4.4,
                "description": "Gentle gel cleanser with soy proteins and cucumber extract.",
                "ingredients": ["Soy Proteins", "Cucumber Extract", "Rose Water"],
                "image": "fresh-soy-cleanser.jpg",
                "category": "cleanser",
                "skin_type": "normal",
                "benefits": ["Gentle", "Makeup removal", "Refreshing", "Natural"],
                "usage": "Apply to damp skin, massage gently, rinse with warm water.",
                "size": "150ml",
                "reviews": 1890
            }
        ],
        "oily": [
            {
                "id": 6,
                "name": "Neutrogena Oil-Free Acne Wash",
                "brand": "Neutrogena",
                "price": 580.17,
                "rating": 4.1,
                "description": "Oil-free cleanser with salicylic acid for oily, acne-prone skin. Clinically proven to clear breakouts.",
                "ingredients": ["Salicylic Acid 2%", "Oil-free formula"],
                "image": "neutrogena-acne-wash.jpg",
                "category": "cleanser",
                "skin_type": "oily",
                "benefits": ["Oil control", "Acne fighting", "Deep cleansing", "Pore clearing"],
                "usage": "Apply to wet skin, massage gently, rinse thoroughly. Use twice daily.",
                "size": "269ml",
                "reviews": 3200
            },
            {
                "id": 7,
                "name": "La Roche-Posay Effaclar Purifying Foaming Gel",
                "brand": "La Roche-Posay",
                "price": 1244.17,
                "rating": 4.4,
                "description": "Purifying foaming gel for oily, sensitive skin. Contains thermal spring water.",
                "ingredients": ["Zinc Pidolate", "Thermal Spring Water", "Soap-free"],
                "image": "lrp-effaclar-gel.jpg",
                "category": "cleanser",
                "skin_type": "oily",
                "benefits": ["Purifying", "Oil control", "Gentle", "Non-drying"],
                "usage": "Apply to wet skin, work into lather, rinse thoroughly.",
                "size": "400ml",
                "reviews": 1567
            },
            {
                "id": 8,
                "name": "Paula's Choice CLEAR Pore Normalizing Cleanser",
                "brand": "Paula's Choice",
                "price": 1494.0,
                "rating": 4.5,
                "description": "Gentle cleanser that removes excess oil without over-drying.",
                "ingredients": ["Ceramides", "Plant Extracts", "Gentle Surfactants"],
                "image": "pc-clear-cleanser.jpg",
                "category": "cleanser",
                "skin_type": "oily",
                "benefits": ["Pore normalizing", "Gentle", "Oil control", "Non-stripping"],
                "usage": "Apply to damp skin, massage gently, rinse with lukewarm water.",
                "size": "177ml",
                "reviews": 987
            }
        ]
    },
    "moisturizer": {
        "dry": [
            {
                "id": 9,
                "name": "CeraVe Daily Moisturizing Lotion",
                "brand": "CeraVe",
                "price": 1410.17,
                "rating": 4.6,
                "description": "24-hour hydrating lotion with ceramides for dry skin. MVE technology provides controlled release.",
                "ingredients": ["Ceramides", "Hyaluronic Acid", "MVE Technology", "Dimethicone"],
                "image": "cerave-daily-lotion.jpg",
                "category": "moisturizer",
                "skin_type": "dry",
                "benefits": ["24-hour hydration", "Restores skin barrier", "Non-greasy", "Fragrance-free"],
                "usage": "Apply liberally to face and body. Use morning and evening.",
                "size": "473ml",
                "reviews": 4500
            },
            {
                "id": 10,
                "name": "Olay Regenerist Micro-Sculpting Cream",
                "brand": "Olay",
                "price": 2406.17,
                "rating": 4.4,
                "description": "Anti-aging moisturizer with amino-peptides and niacinamide.",
                "ingredients": ["Amino-Peptides", "Niacinamide", "Glycerin", "Isohexadecane"],
                "image": "olay-regenerist-cream.jpg",
                "category": "moisturizer",
                "skin_type": "dry",
                "benefits": ["Anti-aging", "Firming", "Hydrating", "Smoothing"],
                "usage": "Apply to clean face and neck morning and evening.",
                "size": "50g",
                "reviews": 2890
            },
            {
                "id": 11,
                "name": "Kiehl's Ultra Facial Cream",
                "brand": "Kiehl's",
                "price": 2573.0,
                "rating": 4.5,
                "description": "24-hour moisturizer suitable for all skin types, especially dry skin.",
                "ingredients": ["Glacial Glycoprotein", "Desert Plant Extracts", "Olive-derived Squalane"],
                "image": "kiehls-ultra-facial.jpg",
                "category": "moisturizer",
                "skin_type": "dry",
                "benefits": ["24-hour moisture", "All weather protection", "Non-greasy"],
                "usage": "Apply to clean skin morning and evening.",
                "size": "50ml",
                "reviews": 1678
            }
        ],
        "normal": [
            {
                "id": 12,
                "name": "Neutrogena Hydro Boost Water Gel",
                "brand": "Neutrogena",
                "price": 1576.17,
                "rating": 4.4,
                "description": "Lightweight water gel moisturizer for normal skin. Oil-free and non-comedogenic.",
                "ingredients": ["Hyaluronic Acid", "Olive Extract", "Dimethicone"],
                "image": "neutrogena-hydro-boost.jpg",
                "category": "moisturizer",
                "skin_type": "normal",
                "benefits": ["Lightweight", "Hydrating", "Non-comedogenic", "Quick absorption"],
                "usage": "Apply to clean face morning and evening.",
                "size": "50g",
                "reviews": 3456
            },
            {
                "id": 13,
                "name": "Clinique Moisture Surge 72-Hour Auto-Replenishing Hydrator",
                "brand": "Clinique",
                "price": 3237.0,
                "rating": 4.3,
                "description": "72-hour hydration with auto-replenishing technology.",
                "ingredients": ["Hyaluronic Acid", "Aloe Bioferment", "Caffeine"],
                "image": "clinique-moisture-surge.jpg",
                "category": "moisturizer",
                "skin_type": "normal",
                "benefits": ["72-hour hydration", "Auto-replenishing", "Cooling", "Plumping"],
                "usage": "Apply twice daily to clean skin.",
                "size": "50ml",
                "reviews": 2134
            }
        ],
        "oily": [
            {
                "id": 14,
                "name": "Clinique Dramatically Different Moisturizing Gel",
                "brand": "Clinique",
                "price": 2489.17,
                "rating": 4.3,
                "description": "Oil-free moisturizing gel for oily skin. Lightweight and fast-absorbing.",
                "ingredients": ["Hyaluronic Acid", "Cucumber Extract", "Barley Extract"],
                "image": "clinique-dd-gel.jpg",
                "category": "moisturizer",
                "skin_type": "oily",
                "benefits": ["Oil-free", "Lightweight", "Non-comedogenic", "Fast-absorbing"],
                "usage": "Apply to clean skin morning and evening.",
                "size": "50ml",
                "reviews": 1890
            },
            {
                "id": 15,
                "name": "Neutrogena Oil-Free Moisture Gel",
                "brand": "Neutrogena",
                "price": 744.51,
                "rating": 4.2,
                "description": "Lightweight, oil-free moisturizer for combination to oily skin.",
                "ingredients": ["Glycerin", "Dimethicone", "Carbomer"],
                "image": "neutrogena-oil-free-gel.jpg",
                "category": "moisturizer",
                "skin_type": "oily",
                "benefits": ["Oil-free", "Non-comedogenic", "Lightweight", "Quick-absorbing"],
                "usage": "Apply to clean face and neck twice daily.",
                "size": "118ml",
                "reviews": 2567
            },
            {
                "id": 16,
                "name": "The Ordinary Natural Moisturizing Factors + HA",
                "brand": "The Ordinary",
                "price": 655.7,
                "rating": 4.1,
                "description": "Lightweight moisturizer with natural moisturizing factors and hyaluronic acid.",
                "ingredients": ["Hyaluronic Acid", "Amino Acids", "Fatty Acids", "Triglycerides"],
                "image": "to-nmf-ha.jpg",
                "category": "moisturizer",
                "skin_type": "oily",
                "benefits": ["Lightweight", "Natural ingredients", "Non-greasy", "Affordable"],
                "usage": "Apply to entire face morning and evening.",
                "size": "100ml",
                "reviews": 4567
            }
        ]
    },
    "serum": [
        {
            "id": 17,
            "name": "The Ordinary Niacinamide 10% + Zinc 1%",
            "brand": "The Ordinary",
            "price": 597.6,
            "rating": 4.2,
            "description": "High-strength niacinamide serum for blemish-prone skin. Reduces appearance of skin blemishes and congestion.",
            "ingredients": ["Niacinamide 10%", "Zinc PCA 1%"],
            "image": "to-niacinamide.jpg",
            "category": "serum",
            "skin_type": "all",
            "benefits": ["Reduces blemishes", "Controls oil", "Minimizes pores", "Brightening"],
            "usage": "Apply to entire face morning and evening before heavier creams.",
            "size": "30ml",
            "reviews": 8900
        },
        {
            "id": 18,
            "name": "The Ordinary Hyaluronic Acid 2% + B5",
            "brand": "The Ordinary",
            "price": 738.7,
            "rating": 4.5,
            "description": "Multi-molecular hyaluronic acid serum for hydration. Multiple types of HA for comprehensive hydration.",
            "ingredients": ["Hyaluronic Acid 2%", "Vitamin B5", "Sodium Hyaluronate"],
            "image": "to-hyaluronic.jpg",
            "category": "serum",
            "skin_type": "all",
            "benefits": ["Deep hydration", "Plumping", "Anti-aging", "Smooth texture"],
            "usage": "Apply to damp skin before oils and creams. Use morning and evening.",
            "size": "30ml",
            "reviews": 7654
        },
        {
            "id": 19,
            "name": "Paula's Choice 2% BHA Liquid Exfoliant",
            "brand": "Paula's Choice",
            "price": 2656.0,
            "rating": 4.6,
            "description": "Leave-on BHA exfoliant that unclogs pores and smooths wrinkles.",
            "ingredients": ["Salicylic Acid 2%", "Green Tea Extract"],
            "image": "pc-bha-liquid.jpg",
            "category": "serum",
            "skin_type": "oily",
            "benefits": ["Exfoliating", "Pore clearing", "Anti-aging", "Blackhead removal"],
            "usage": "Apply with cotton pad or hands after cleansing. Use evening only initially.",
            "size": "118ml",
            "reviews": 5432
        },
        {
            "id": 20,
            "name": "Skinceuticals CE Ferulic",
            "brand": "SkinCeuticals",
            "price": 14027.0,
            "rating": 4.7,
            "description": "Antioxidant serum with 15% L-Ascorbic Acid, 1% Vitamin E, and 0.5% Ferulic Acid.",
            "ingredients": ["L-Ascorbic Acid 15%", "Vitamin E 1%", "Ferulic Acid 0.5%"],
            "image": "skinceuticals-ce.jpg",
            "category": "serum",
            "skin_type": "all",
            "benefits": ["Antioxidant protection", "Anti-aging", "Brightening", "Collagen synthesis"],
            "usage": "Apply 4-5 drops to clean skin in the morning before moisturizer.",
            "size": "30ml",
            "reviews": 2890
        },
        {
            "id": 21,
            "name": "The Ordinary Retinol 0.5% in Squalane",
            "brand": "The Ordinary",
            "price": 821.7,
            "rating": 4.3,
            "description": "Moderate-strength retinol serum for anti-aging benefits.",
            "ingredients": ["Retinol 0.5%", "Squalane"],
            "image": "to-retinol.jpg",
            "category": "serum",
            "skin_type": "all",
            "benefits": ["Anti-aging", "Texture improvement", "Fine lines", "Cell turnover"],
            "usage": "Apply to face in the evening only. Start with 2-3 times per week.",
            "size": "30ml",
            "reviews": 3456
        }
    ],
    "sunscreen": [
        {
            "id": 22,
            "name": "EltaMD UV Clear Broad-Spectrum SPF 46",
            "brand": "EltaMD",
            "price": 3071.0,
            "rating": 4.7,
            "description": "Lightweight sunscreen with niacinamide for sensitive skin. Zinc oxide and octinoxate provide broad spectrum protection.",
            "ingredients": ["Zinc Oxide 9%", "Octinoxate 7.5%", "Niacinamide", "Hyaluronic Acid"],
            "image": "eltamd-uv-clear.jpg",
            "category": "sunscreen",
            "skin_type": "all",
            "benefits": ["Broad spectrum", "Lightweight", "Anti-aging", "Sensitive skin"],
            "usage": "Apply liberally 15 minutes before sun exposure. Reapply every 2 hours.",
            "size": "48g",
            "reviews": 3890
        },
        {
            "id": 23,
            "name": "La Roche-Posay Anthelios Melt-in Milk Sunscreen SPF 60",
            "brand": "La Roche-Posay",
            "price": 2987.17,
            "rating": 4.5,
            "description": "Fast-absorbing sunscreen with antioxidants. Water-resistant for 80 minutes.",
            "ingredients": ["Avobenzone 3%", "Homosalate 15%", "Octisalate 5%", "Antioxidants"],
            "image": "lrp-anthelios.jpg",
            "category": "sunscreen",
            "skin_type": "all",
            "benefits": ["Fast-absorbing", "Water-resistant", "Antioxidant protection", "Non-greasy"],
            "usage": "Apply generously and evenly before sun exposure. Reapply frequently.",
            "size": "150ml",
            "reviews": 2567
        },
        {
            "id": 24,
            "name": "Neutrogena Ultra Sheer Dry-Touch Sunscreen SPF 100+",
            "brand": "Neutrogena",
            "price": 910.51,
            "rating": 4.3,
            "description": "Dry-touch sunscreen with Helioplex technology for superior protection.",
            "ingredients": ["Avobenzone 3%", "Homosalate 15%", "Octisalate 5%", "Oxybenzone 6%"],
            "image": "neutrogena-ultra-sheer.jpg",
            "category": "sunscreen",
            "skin_type": "all",
            "benefits": ["High SPF", "Dry-touch", "Water-resistant", "Non-comedogenic"],
            "usage": "Apply liberally 15 minutes before sun exposure. Reapply every 2 hours.",
            "size": "88ml",
            "reviews": 4567
        },
        {
            "id": 25,
            "name": "CeraVe Hydrating Mineral Sunscreen SPF 30",
            "brand": "CeraVe",
            "price": 1244.17,
            "rating": 4.4,
            "description": "Mineral sunscreen with ceramides and hyaluronic acid for hydration.",
            "ingredients": ["Zinc Oxide 10.7%", "Titanium Dioxide 5%", "Ceramides", "Hyaluronic Acid"],
            "image": "cerave-mineral-spf.jpg",
            "category": "sunscreen",
            "skin_type": "dry",
            "benefits": ["Mineral protection", "Hydrating", "Sensitive skin", "Reef-safe"],
            "usage": "Apply liberally to face and body 15 minutes before sun exposure.",
            "size": "75ml",
            "reviews": 1890
        }
    ],
    "treatment": [
        {
            "id": 26,
            "name": "Differin Adapalene Gel 0.1%",
            "brand": "Differin",
            "price": 1069.04,
            "rating": 4.4,
            "description": "Prescription-strength retinoid for acne treatment. FDA-approved adapalene gel.",
            "ingredients": ["Adapalene 0.1%"],
            "image": "differin-gel.jpg",
            "category": "treatment",
            "skin_type": "oily",
            "benefits": ["Acne treatment", "Prevents breakouts", "Unclogs pores", "Anti-aging"],
            "usage": "Apply thin layer to affected areas once daily in the evening.",
            "size": "45g",
            "reviews": 6789
        },
        {
            "id": 27,
            "name": "Mario Badescu Drying Lotion",
            "brand": "Mario Badescu",
            "price": 1411.0,
            "rating": 4.2,
            "description": "Overnight spot treatment for blemishes with salicylic acid and zinc oxide.",
            "ingredients": ["Salicylic Acid", "Zinc Oxide", "Sulfur"],
            "image": "mb-drying-lotion.jpg",
            "category": "treatment",
            "skin_type": "oily",
            "benefits": ["Spot treatment", "Overnight healing", "Reduces inflammation", "Quick results"],
            "usage": "Dip cotton swab to bottom, dab on blemish, leave overnight.",
            "size": "29ml",
            "reviews": 3456
        }
    ],
    "mask": [
        {
            "id": 28,
            "name": "The Ordinary AHA 30% + BHA 2% Peeling Solution",
            "brand": "The Ordinary",
            "price": 705.5,
            "rating": 4.3,
            "description": "Weekly exfoliating treatment with alpha and beta hydroxy acids.",
            "ingredients": ["Glycolic Acid", "Lactic Acid", "Salicylic Acid", "Hyaluronic Acid"],
            "image": "to-peeling-solution.jpg",
            "category": "mask",
            "skin_type": "all",
            "benefits": ["Deep exfoliation", "Brightening", "Texture improvement", "Pore refining"],
            "usage": "Apply to clean, dry skin for maximum 10 minutes once per week.",
            "size": "30ml",
            "reviews": 5678
        },
        {
            "id": 29,
            "name": "Origins Clear Improvement Charcoal Honey Mask",
            "brand": "Origins",
            "price": 2822.0,
            "rating": 4.5,
            "description": "Purifying mask with bamboo charcoal and white China clay.",
            "ingredients": ["Bamboo Charcoal", "White China Clay", "Honey"],
            "image": "origins-charcoal-mask.jpg",
            "category": "mask",
            "skin_type": "oily",
            "benefits": ["Deep cleansing", "Pore minimizing", "Oil control", "Purifying"],
            "usage": "Apply to clean skin, leave for 10 minutes, rinse with warm water.",
            "size": "75ml",
            "reviews": 2345
        },
        {
            "id": 30,
            "name": "Laneige Water Sleeping Mask",
            "brand": "Laneige",
            "price": 2822.0,
            "rating": 4.6,
            "description": "Overnight hydrating mask with Sleep-tox technology.",
            "ingredients": ["Hydro Ionized Mineral Water", "Evening Primrose Root Extract", "Hunza Apricot Extract"],
            "image": "laneige-sleeping-mask.jpg",
            "category": "mask",
            "skin_type": "dry",
            "benefits": ["Overnight hydration", "Skin repair", "Brightening", "Plumping"],
            "usage": "Apply as last step of evening routine 2-3 times per week.",
            "size": "70ml",
            "reviews": 4567
        }
    ]
}

def get_products_by_category(category, skin_type=None):
    """Get products by category and optionally filter by skin type"""
    if category not in SKINCARE_PRODUCTS:
        return []
    
    products = SKINCARE_PRODUCTS[category]
    
    # Handle nested structure for cleanser and moisturizer
    if isinstance(products, dict):
        if skin_type and skin_type in products:
            return products[skin_type]
        else:
            # Return all products from all skin types
            all_products = []
            for skin_products in products.values():
                all_products.extend(skin_products)
            return all_products
    else:
        # Handle flat structure for serum, sunscreen, treatment, mask
        if skin_type and skin_type != 'all':
            return [p for p in products if p['skin_type'] == 'all' or p['skin_type'] == skin_type]
        return products

def search_products(query):
    """Search products by name, brand, ingredients, or benefits"""
    results = []
    query = query.lower()
    
    for category, products in SKINCARE_PRODUCTS.items():
        if isinstance(products, dict):
            # Handle nested structure
            for skin_type, skin_products in products.items():
                for product in skin_products:
                    if (query in product['name'].lower() or 
                        query in product['brand'].lower() or 
                        query in product['description'].lower() or
                        any(query in ingredient.lower() for ingredient in product['ingredients']) or
                        any(query in benefit.lower() for benefit in product['benefits'])):
                        results.append(product)
        else:
            # Handle flat structure
            for product in products:
                if (query in product['name'].lower() or 
                    query in product['brand'].lower() or 
                    query in product['description'].lower() or
                    any(query in ingredient.lower() for ingredient in product['ingredients']) or
                    any(query in benefit.lower() for benefit in product['benefits'])):
                    results.append(product)
    
    return results

def get_product_by_id(product_id):
    """Get a specific product by ID"""
    for category, products in SKINCARE_PRODUCTS.items():
        if isinstance(products, dict):
            for skin_type, skin_products in products.items():
                for product in skin_products:
                    if product['id'] == product_id:
                        return product
        else:
            for product in products:
                if product['id'] == product_id:
                    return product
    return None

def get_recommended_products(skin_type, issues=None):
    """Get AI-powered recommended products based on skin type and issues"""
    recommendations = []
    
    # Essential routine: cleanser, moisturizer, sunscreen
    cleanser = get_products_by_category('cleanser', skin_type)
    if cleanser:
        # Get top-rated cleanser for skin type
        top_cleanser = max(cleanser, key=lambda x: x['rating'])
        recommendations.append(top_cleanser)
    
    moisturizer = get_products_by_category('moisturizer', skin_type)
    if moisturizer:
        # Get top-rated moisturizer for skin type
        top_moisturizer = max(moisturizer, key=lambda x: x['rating'])
        recommendations.append(top_moisturizer)
    
    # Always recommend sunscreen (essential for all skin types)
    sunscreen = get_products_by_category('sunscreen')
    if sunscreen:
        # Prefer sunscreen suitable for skin type, fallback to highest rated
        suitable_sunscreen = [s for s in sunscreen if s['skin_type'] == skin_type or s['skin_type'] == 'all']
        if suitable_sunscreen:
            top_sunscreen = max(suitable_sunscreen, key=lambda x: x['rating'])
        else:
            top_sunscreen = max(sunscreen, key=lambda x: x['rating'])
        recommendations.append(top_sunscreen)
    
    # Add targeted treatments based on issues
    if issues:
        serums = get_products_by_category('serum')
        treatments = get_products_by_category('treatment')
        
        for issue in issues:
            if issue.lower() in ['acne', 'breakouts', 'blemishes']:
                # Recommend niacinamide for acne/oil control
                niacinamide_products = [s for s in serums if 'niacinamide' in s['name'].lower()]
                if niacinamide_products:
                    recommendations.append(max(niacinamide_products, key=lambda x: x['rating']))
                
                # Add acne treatment if oily skin
                if skin_type == 'oily':
                    acne_treatments = [t for t in treatments if 'acne' in t['description'].lower()]
                    if acne_treatments:
                        recommendations.append(max(acne_treatments, key=lambda x: x['rating']))
            
            elif issue.lower() in ['dullness', 'uneven tone', 'dark spots']:
                # Recommend vitamin C for brightening
                vitamin_c_products = [s for s in serums if 'vitamin c' in s['description'].lower() or 'ascorbic' in s['name'].lower()]
                if vitamin_c_products:
                    recommendations.append(max(vitamin_c_products, key=lambda x: x['rating']))
            
            elif issue.lower() in ['dryness', 'dehydration']:
                # Recommend hyaluronic acid for hydration
                ha_products = [s for s in serums if 'hyaluronic' in s['name'].lower()]
                if ha_products:
                    recommendations.append(max(ha_products, key=lambda x: x['rating']))
            
            elif issue.lower() in ['aging', 'wrinkles', 'fine lines']:
                # Recommend retinol for anti-aging
                retinol_products = [s for s in serums if 'retinol' in s['name'].lower()]
                if retinol_products:
                    recommendations.append(max(retinol_products, key=lambda x: x['rating']))
    
    # Remove duplicates while preserving order
    seen = set()
    unique_recommendations = []
    for product in recommendations:
        if product['id'] not in seen:
            seen.add(product['id'])
            unique_recommendations.append(product)
    
    return unique_recommendations

def get_product_categories():
    """Get all available product categories"""
    return list(SKINCARE_PRODUCTS.keys())

def get_products_by_price_range(min_price=0, max_price=1000):
    """Get products within a specific price range"""
    results = []
    
    for category, products in SKINCARE_PRODUCTS.items():
        if isinstance(products, dict):
            for skin_type, skin_products in products.items():
                for product in skin_products:
                    if min_price <= product['price'] <= max_price:
                        results.append(product)
        else:
            for product in products:
                if min_price <= product['price'] <= max_price:
                    results.append(product)
    
    return sorted(results, key=lambda x: x['price'])

def get_top_rated_products(limit=10):
    """Get top-rated products across all categories"""
    all_products = []
    
    for category, products in SKINCARE_PRODUCTS.items():
        if isinstance(products, dict):
            for skin_type, skin_products in products.items():
                all_products.extend(skin_products)
        else:
            all_products.extend(products)
    
    # Sort by rating and return top products
    return sorted(all_products, key=lambda x: x['rating'], reverse=True)[:limit]