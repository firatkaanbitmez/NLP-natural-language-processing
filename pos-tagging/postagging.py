import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from nltk.tokenize import word_tokenize
from nltk import pos_tag
# Bu alanda Veri kümesini yükleme ve ön işleme
# Veri kümesinin yüklenmesi, temizlenmesi ve POS etiketlerinin alınması işlemleri burada gerçekleştirilir.
# Özellik vektörlerinin oluşturulması
# Her kelime için özellik vektörleri oluşturulur. Bu özellik vektörleri, kelimenin uzunluğu, büyük/küçük harf
olması gibi özellikleri içerir. Ama bizim amacımız bu tasarımda YSA aşamasına odaklanmak olduğu için bu
adımları atlayacağız.
# Yapay sinir ağı (YSA) modelinin tanımlanması
model = models.Sequential([
layers.Dense(128, activation='relu', input_shape=(feature_vector_size,)),
layers.Dense(64, activation='relu'),
layers.Dense(num_classes, activation='softmax')
])
# Modelin derlenmesi
model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy'])
# Modelin eğitilmesi
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))
# Modelin değerlendirilmesi
test_loss, test_accuracy = model.evaluate(X_test, y_test)