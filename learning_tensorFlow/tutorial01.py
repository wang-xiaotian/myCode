import tensorflow.compat.v1 as tf
'''
according to tensorflow symbols map 
https://docs.google.com/spreadsheets/d/1FLFJLzg7WNP6JHODX5q8BDgptKafq_slHpnHVbJIteQ/edit#gid=0
'''
tf.disable_v2_behavior()

# initialize two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

# multiply
result = tf.multiply(x1,x2)
print(result)

# intialize the session
with tf.Session() as sess:
    print(sess.run(result))
