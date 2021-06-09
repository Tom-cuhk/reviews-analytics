data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))
print('There are total ', len(data), 'reviews')

i = 0
word = 0
while i < len(data):
	word = word + len(data[i].split()) #To calculate the number of word (not the number of letter)
	i += 1
print('The average number of word in each review is ', word/len(data))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('The average number of letter in each review is ', sum_len/len(data))

# to screen the review by the number of words or letters

new1 = []
new2 = []
l = 0
w = 0
for d in data:
	if len(d) > 200:
		new1.append(d)
		l += 1
	if len(d.split()) >100:
		new2.append(d)
		w += 1
print('There are ', l, 'comments with more than 200 letters.')
print('There are ', w, 'comments with more than 100 words')
print('Total ', len(new1), 'comments with more than 200 letters')
print(new1[0])
print('Total ', len(new2), 'comments with more than 100 words')
print(new2[0])