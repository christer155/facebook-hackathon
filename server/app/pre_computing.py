from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
def stemming():
    ps = PorterStemmer()
    input_tweet = 'testing tests trying tries'
    words = word_tokenize(input_tweet)

    for w in words:
     print(ps.stem(words))

def animate(computed_data):

    lines = computed_data.split('\n')

    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines[-200:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xar.append(x)
        yar.append(y)

    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()