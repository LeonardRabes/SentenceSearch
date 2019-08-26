import tensorflow as tf

def create_model_cnn():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv1D(kernel_size=128, filters=32, activation=tf.nn.relu))
    model.add(tf.keras.layers.MaxPooling1D(2))
    model.add(tf.keras.layers.Conv1D(kernel_size=64, filters=16, activation=tf.nn.relu))
    model.add(tf.keras.layers.MaxPooling1D(2))
    model.add(tf.keras.layers.Conv1D(kernel_size=16, filters=8, activation=tf.nn.relu))
    model.add(tf.keras.layers.MaxPooling1D(2))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(2, activation=tf.nn.sigmoid))

    opt = tf.keras.optimizers.Adam(lr=1e-3)
    model.compile(optimizer=opt,
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model

def create_model_nn():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(1000, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(500, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(2, activation=tf.nn.sigmoid))

    opt = tf.keras.optimizers.Adam(lr=1e-3)
    model.compile(optimizer=opt,
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model

def create_model_gru():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.CuDNNLSTM(32, input_shape=(129600, 1), return_sequences=True))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.BatchNormalization())

    model.add(tf.keras.layers.CuDNNLSTM(32, input_shape=(129600, 1), return_sequences=True))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.BatchNormalization())

    model.add(tf.keras.layers.CuDNNLSTM(32, input_shape=(129600, 1)))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.BatchNormalization())

    model.add(tf.keras.layers.Dense(32, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(2, activation=tf.nn.sigmoid))

    opt = tf.keras.optimizers.Adam(lr=1e-3)
    model.compile(optimizer=opt,
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model
