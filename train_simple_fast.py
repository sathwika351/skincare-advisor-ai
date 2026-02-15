#!/usr/bin/env python3
"""
Simple Fast Training for Better Accuracy
This script trains a model quickly with good accuracy
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import os
from datetime import datetime

# Set random seeds
tf.random.set_seed(42)
np.random.seed(42)

def create_simple_model(img_size=(224, 224), num_classes=3):
    """Create a simple but effective model"""
    
    model = tf.keras.Sequential([
        # Input layer
        layers.Input(shape=(*img_size, 3)),
        
        # Feature extraction
        layers.Conv2D(32, 3, activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D(2),
        layers.Dropout(0.25),
        
        layers.Conv2D(64, 3, activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D(2),
        layers.Dropout(0.25),
        
        layers.Conv2D(128, 3, activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D(2),
        layers.Dropout(0.25),
        
        layers.Conv2D(256, 3, activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.GlobalAveragePooling2D(),
        
        # Classification
        layers.Dense(512, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        
        layers.Dense(num_classes, activation='softmax')
    ])
    
    return model

def simple_train():
    """Simple training function"""
    print("🚀 Simple Fast Training")
    print("=" * 30)
    
    # Check data
    if not os.path.exists("Oily-Dry-Skin-Types"):
        print("❌ Training data not found!")
        return None, 0
    
    # Parameters
    IMG_SIZE = (224, 224)
    BATCH_SIZE = 32
    EPOCHS = 15
    
    print("📊 Loading data...")
    
    # Data generators
    train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.15,
        height_shift_range=0.15,
        zoom_range=0.15,
        horizontal_flip=True,
        brightness_range=[0.9, 1.1]
    )
    
    val_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
    
    # Load data
    train_data = train_datagen.flow_from_directory(
        'Oily-Dry-Skin-Types/train',
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )
    
    val_data = val_datagen.flow_from_directory(
        'Oily-Dry-Skin-Types/valid',
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )
    
    test_data = val_datagen.flow_from_directory(
        'Oily-Dry-Skin-Types/test',
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        shuffle=False
    )
    
    print(f"✅ Training samples: {train_data.samples}")
    print(f"✅ Validation samples: {val_data.samples}")
    print(f"✅ Test samples: {test_data.samples}")
    
    # Create model
    print("🏗️  Creating model...")
    model = create_simple_model(IMG_SIZE, 3)
    
    # Compile model
    model.compile(
        optimizer=tf.keras.optimizers.Adam(0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("📋 Model Summary:")
    model.summary()
    
    # Simple callbacks
    callbacks = [
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss', factor=0.2, patience=3, min_lr=1e-7
        ),
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss', patience=5, restore_best_weights=True
        )
    ]
    
    # Train model
    print(f"🚀 Training for {EPOCHS} epochs...")
    
    history = model.fit(
        train_data,
        epochs=EPOCHS,
        validation_data=val_data,
        callbacks=callbacks,
        verbose=1
    )
    
    # Evaluate
    print("📊 Evaluating model...")
    test_loss, test_accuracy = model.evaluate(test_data, verbose=1)
    
    print(f"\n🎯 Results:")
    print(f"   Test Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.1f}%)")
    print(f"   Test Loss: {test_loss:.4f}")
    
    # Save model
    os.makedirs('model', exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_path = f'model/simple_model_{timestamp}.h5'
    
    try:
        model.save(model_path)
        model.save('model/simple_effective_model.h5')
        print(f"💾 Model saved: {model_path}")
        print(f"💾 Default model updated: model/simple_effective_model.h5")
    except Exception as e:
        print(f"⚠️  Error saving model: {e}")
    
    # Performance assessment
    if test_accuracy > 0.80:
        print("🏆 Excellent performance!")
    elif test_accuracy > 0.70:
        print("✅ Good performance!")
    elif test_accuracy > 0.60:
        print("⚠️  Acceptable performance")
    else:
        print("❌ Low performance")
    
    return model, test_accuracy

def test_model():
    """Test the trained model"""
    print("\n🧪 Testing model...")
    
    model_path = 'model/simple_effective_model.h5'
    if not os.path.exists(model_path):
        print("❌ No trained model found")
        return
    
    try:
        model = tf.keras.models.load_model(model_path)
        class_names = ['dry', 'normal', 'oily']
        
        # Test on sample images
        test_dirs = ['Oily-Dry-Skin-Types/test/dry', 'Oily-Dry-Skin-Types/test/normal', 'Oily-Dry-Skin-Types/test/oily']
        
        correct_predictions = 0
        total_predictions = 0
        
        for test_dir in test_dirs:
            if os.path.exists(test_dir):
                true_class = os.path.basename(test_dir)
                images = os.listdir(test_dir)[:5]  # Test first 5 images
                
                print(f"\n📁 Testing {true_class.upper()} images:")
                
                for img_name in images:
                    img_path = os.path.join(test_dir, img_name)
                    
                    # Load and preprocess image
                    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
                    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
                    img_array = np.expand_dims(img_array, axis=0)
                    
                    # Predict
                    predictions = model.predict(img_array, verbose=0)
                    predicted_class = class_names[np.argmax(predictions[0])]
                    confidence = np.max(predictions[0])
                    
                    status = "✅" if predicted_class == true_class else "❌"
                    print(f"   {status} {img_name}: {predicted_class} ({confidence:.3f})")
                    
                    if predicted_class == true_class:
                        correct_predictions += 1
                    total_predictions += 1
        
        if total_predictions > 0:
            accuracy = correct_predictions / total_predictions
            print(f"\n📊 Sample Test Accuracy: {accuracy:.3f} ({accuracy*100:.1f}%)")
                    
    except Exception as e:
        print(f"❌ Error testing model: {e}")

if __name__ == "__main__":
    model, accuracy = simple_train()
    if model:
        print(f"\n🎉 Training completed with {accuracy:.1%} accuracy!")
        test_model()
    else:
        print("❌ Training failed!")