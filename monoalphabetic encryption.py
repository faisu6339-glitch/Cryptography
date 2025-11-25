l = [x for x in range(97,123)]
alphabets = [chr(x) for x in l]
pos_values = [x for x in range(26)]
text = dict(zip(alphabets, pos_values))
value = dict(zip(pos_values, alphabets))