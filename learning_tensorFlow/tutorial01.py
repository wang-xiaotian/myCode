import tensorflow as tf

'''
scalar, vector, matrix and tensor
a tensor is a vector or a matrix of n-dimensions(ranks) that represents all types of data
What's a Tensor? https://www.youtube.com/watch?v=f5liqUk0ZTw
'''
# initialize two constants
c1 = tf.constant([[1,2], [3,4]])
print(c1)

v1 = tf.Variable([[1,2], [3,4]])
print(v1)

'''
tf.float16: 16-bit half-precision floating-point.
tf.float32: 32-bit single-precision floating-point.
tf.float64: 64-bit double-precision floating-point.
tf.bfloat16: 16-bit truncated floating-point.
tf.complex64: 64-bit single-precision complex.
tf.complex128: 128-bit double-precision complex.
tf.int8: 8-bit signed integer.
tf.uint8: 8-bit unsigned integer.
tf.uint16: 16-bit unsigned integer.
tf.uint32: 32-bit unsigned integer.
tf.uint64: 64-bit unsigned integer.
tf.int16: 16-bit signed integer.
tf.int32: 32-bit signed integer.
tf.int64: 64-bit signed integer.
tf.bool: Boolean.
tf.string: String.
tf.qint8: Quantized 8-bit signed integer.
tf.quint8: Quantized 8-bit unsigned integer.
tf.qint16: Quantized 16-bit signed integer.
tf.quint16: Quantized 16-bit unsigned integer.
tf.qint32: Quantized 32-bit signed integer.
tf.resource: Handle to a mutable resource.
tf.variant: Values of arbitrary types.
'''

# multiply
result = tf.matmul(c1,v1)
# result.op is meaningless when eager execution is enabled
# so uee .numpy
print(f'\n\n{c1.numpy()}\n*\n{v1.numpy()}\n=\n{result.numpy()}\n\n')

# concatenate by columns
concat_columns = tf.concat(values=[c1, v1], axis=1)
print(f'colums concatenantion:\n{concat_columns}\n')

# concatenate by rows
concat_rows = tf.concat(values=[c1, v1], axis=0)
print(f'rows concatenation:\n{concat_rows}\n')


concat_rows_cast = tf.cast(concat_rows, tf.float32)
rows, columns = concat_rows_cast.shape

print(concat_rows_cast)
print(f'# of rows: {rows} and # of columns: {columns}')

concat_rows_cast_reshape = tf.transpose(concat_rows_cast)
rows, columns = concat_rows_cast_reshape.shape

print(concat_rows_cast_reshape)
print(f'# of rows: {rows} and # of columns: {columns}')

''' 
in tensorflow 1.0, a session runs a computational graph
in tensorflow 2.0, we only use model.fit(...) to let data flow throgh layers

a computational graph is how one 'layer' is transformed to another 'layer'
layers are different phases of my data
layers can be sequencial, functional or subclassing which provided by tf.keras (high level API of tf 2.0)
'''

# available math function in tensorflow
print(dir(tf.math))