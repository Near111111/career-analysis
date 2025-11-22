import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("=" * 60)
print("CAREER PREDICTION MODEL TRAINER")
print("=" * 60)

# Load dataset
print("\n📂 Loading dataset...")
try:
    df = pd.read_csv("career_dataset.csv")
    print(f"✓ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"✓ Unique careers: {df['Career'].nunique()}")
except Exception as e:
    print(f"✗ Error loading dataset: {e}")
    exit(1)

# Prepare features and labels
X = df[[f"Q{i}" for i in range(1, 13)]]
y = df["Career"]

print(f"\n✓ Features shape: {X.shape}")
print(f"✓ Labels shape: {y.shape}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\n✓ Training set: {len(X_train)} samples")
print(f"✓ Test set: {len(X_test)} samples")

# Train Random Forest Model
print("\n🔄 Training Random Forest model...")
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)
print("✓ Model trained successfully!")

# Evaluate model
print("\n📊 Evaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n🎯 Model Accuracy: {accuracy * 100:.2f}%")

# Detailed report (optional, comment out if too long)
# print("\n📋 Classification Report:")
# print(classification_report(y_test, y_pred, zero_division=0))

# Save the trained model
print("\n💾 Saving model...")
model_dir = "model"
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, "career_model.pkl")

with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"✓ Model saved to: {model_path}")

# Save model metadata
metadata = {
    'accuracy': accuracy,
    'n_careers': df['Career'].nunique(),
    'n_features': 12,
    'model_type': 'RandomForestClassifier',
    'n_estimators': 200
}

metadata_path = os.path.join(model_dir, "model_metadata.pkl")
with open(metadata_path, 'wb') as f:
    pickle.dump(metadata, f)

print(f"✓ Metadata saved to: {metadata_path}")

# Test the saved model
print("\n🧪 Testing saved model...")
with open(model_path, 'rb') as f:
    loaded_model = pickle.load(f)

# Test prediction
test_input = [[5, 5, 5, 3, 2, 4, 4, 4, 2, 1, 4, 3]]
test_pred = loaded_model.predict(test_input)
print(f"✓ Test prediction successful: {test_pred[0]}")

print("\n" + "=" * 60)
print("✨ MODEL TRAINING COMPLETE!")
print("=" * 60)
print(f"\n📁 Model file: {model_path}")
print(f"📁 Metadata file: {metadata_path}")
print(f"🎯 Accuracy: {accuracy * 100:.2f}%")
print("\n💡 You can now use this model in your Flask app!")
print("=" * 60)