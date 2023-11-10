#WWDC: A3: DAYS 1-14 POEM SENTIMENTS

#DAY 1: Tuesday 17th 4:25pm 
#Location: UTS building 10 
#Mood: Discouraged

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''My hands never used to get this dry 
Everything used to work so beautifully 
The crows used to sound like a choir 
A good one 
A reminder 
I hate that I’m lamenting 
I always call myself out when I do that 
It’s not that my hands were never dry 
It’s just that I never used to feel the need to use hand cream 
Now I’ve smothered myself in things 
Like medicines and the breath of strangers in public places 
I used to be free of all of those things 
I used to think I could strangle the day 
And beat it to beautiful pulp
And drip it’s juices into my mouth 
I used to think that hard 
What a childish thing.'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 2: Wednesday 18th 12:41pm
#Location: UTS Building 10
#Mood: In control 

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''Today is Laura Marling 
Saying “clear as all hell” in my ears 
It is the same feeling I get when Im looking out your bathroom window 
Feeling like I could jump right out and not get a drop of toothpaste on this black shirt
Tonight Ill drink a beer
Maybe two 
Maybe two
We’re different now,
Something about the sun 
Something about the beating of breath 
Something about that atom that just touched me right 
It will be a good day today
No, 
An okay day today 
You know how I feel about expectations 
It will be an okay day today
I will drink all the grit from my coffee cup and know that it won’t kill me 
You’re just so damn delicious 
I will also drink two beers tonight 
And smile I think'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 3: Thursday 19th 5:04pm
#Location: Home
#Mood: Discouraged

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''Maybe one more chocolate-covered almond is what I need 
My answers are never simple 
They always require a chemical equation and a dip in the ocean 
I’ll give you a dollar and a kiss if the sun sets tonight 
I feel it will stay 
I feel it will stay and you’ll never leave the beach 
You will stay perched on that knoll 
Reading that book you don’t really love
With salt forming a constellation across your shoulders 
And the dirt making its sorry home under your toenails
And oxygen,'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 4: Friday 20th 9:16am
#Location: Home
#Mood: Discouraged

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''I wish this coffee tasted better 
That’s a lie 
I wish it wasn’t 9:16am 
Thats the truth
Holding out 
That’s what I’ll do 
Until I die 
That’s the truth  
This is coffee might never get cold 
That’s a lie 
The same ones we tell ourselves all the time
Like we’ll take down the lost cat posters  tomorrow'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 5: Saturday 21st 7:23pm
#Location: Home 
#Mood: Good 

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''We’re going to the pub 
There’s a French saying that I just can’t quite translate that’s ringing in my head 
Beautiful dreams about nothing in particular tonight
Stories of patterned lovers 
And silly little things 
I’m a bit drunk 
And I love the taste of the air'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 6: Sunday 22nd 3:00pm
#Location: Bus
#Mood: In Control 

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''I want to drive a bus that’s not in service 
I want speak to that person 
And tell them things that they’ve heard before 
This morning it was just a piece of toast 
Later it will be caramel-covered popcorn 
Not enough coffee and and cool air 
But I’m here
And I know what to do next 
And I know what I’ll have to do right after'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 7: Monday 23rd October 9:46pm
#Location: Bus
#Mood: Good

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''If I don’t wake up tomorrow 
Make a coffee still 
And fill up a never-ending dream 
With images of familiar hallways and kitchen bench tops 
We are never absolved 
Just spat out 
Different 
I’m Blessing you with things you love 
Like pork fat and toast 
And gentle breeze 
I can almost smell it 
The morning.'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 8: Tuesday 24th 11:54am 
#Location: Bus 
#Mood: Distant

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''Today will be the day it changes 
The day the sun doesn’t feel so hot against my skin 
If I keep asking will you answer 
Will I ever have to not ask?
If I could keep holding on to this baby maybe I could learn to like it 
It won’t stop crying 
And no song I sing will make it hush 
The wailing 
The hysterics 
The damp skin 
The onlookers 
Their disappointed faces 

It’s Tuesday and nothing I do will make it not Tuesday,
Oh the wailing 
Oh the hysterics 
Oh the damp skin 
Oh the onlookers 
Oh their disappointment faces'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 9: Wednesday 25th 5:26pm
#Location: UTS Building 10
#Mood: Ok

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''Travelling backwards on the bus what I needed
To feel the world getting stripped off me 
You don’t get it
How jealous I am
Of your struggle 
You getting whipped up at that intersection 
50 metres off the ground
Never come down 
Flying, 
that’s just walking to you
I forget you can do that too.'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 10: Thursday 26th 4:31pm
#Location: Zoe’s Place 
#Mood: Distant 

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''We were talking about people today 
What we like about them etc.
Why we like those things about them 
Etc.
I couldn’t tell you that the reason I like you so
Is my unfaltering desire
To feel that weight 
To experience my eyelids close each time
I am resting my head on your belly. '''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 11: Friday 27th 3:24pm
#Location: Central Station 
#Mood: In Control 

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''Today it is the coffee
Today it is the protruding shins and hands sitting on top of done buttons 
Spent cash on cash spending stuff
Like petrol and things of the sort 
You’re open and kind because you choose to be 
I’m open and kind because you make me, 
the difference is not the cause, it is the effect 
My heart is in Monte Carlo,
The biscuit.'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 12: Saturday 28th 7:50pm
#Location: Bedroom 
#Mood: Discouraged 

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''Nothing will stop the aching heart 
Or the beating drum 
We are the not the same, I think
And I can’t help but feel stupid
Not knowing the laws of the universe 
And not being able to tell you them all 
Since I can’t use words 
Let me flicker the lights and create ghastly shadows 
Stupid little signs 
That was me just trying to talk to you'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 13: Sunday 29th 4:25pm
#Location: Work
#Mood: Discouraged

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''Ill never be marble in the sun
Nor the faint hum of the refrigerator 
I used to believe you could do anything you wanted to 
Then I started writing and realised that Ill never be not on this side of the laptop 
And that ill never be not brimming with oil and “fuck this”’s.
Im ending this now 
Before I change my mind about my brain, this job, melted wax and buttery pastries. '''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")

#DAY 14: Monday 30th 2:21
#Location: Train
#Mood: Distant 

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download([
    "punkt",
    "stopwords",
])

text = '''All I’ve eaten today are buttery pasties and all I’ve drunk today is tap water and good coffee 
Still addicted to going backwards on trains and buses 
Still too much hurt in these bones 
Too much sorry 
And too many atoms to keep me falling apart like you wanted 
Waking and sleeping 
Bursting and lamenting 
A few of my favourite things'''

stop_list = ["are", "is", "a", "an", "the", "and", "or", "but", "will", "do", "does", "I"]
stpwrd = set(stopwords.words('english') + stop_list)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stpwrd]

cleaned_text = " ".join(filtered_words)

blob = TextBlob(cleaned_text)
sentiment = blob.sentiment.polarity

print(cleaned_text)
print(f"Sentiment: {sentiment}")
