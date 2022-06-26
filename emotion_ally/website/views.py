# store main URL endpoints for front-end; roots (pages not for auth)

from flask import Blueprint, flash, render_template, request
import cohere
co = cohere.Client('4FqDzcvsQz5KGd4E8plG1boeLod3qsEN1Nsk5n6h')
pretext = "i feel that it is something that will never really be resolved;joy\ni just feel like all my efforts are in vain and a waste of time;sadness\ni feel absolutely foolish for allowing myself to actually believe that this might be it for us the month weve been praying so hard for;sadness\ni waited for an eternity for it to download and now im remembering a day when i had to wait to go to walmart to buy a whole cd just to hear one song and feeling kinda dumb with my impatience;sadness\ni don t know if anybody will ever be able to feel how i feel or at least relate when everything is lost you find yourself missing and longing for it them;sadness\ni feel as if i am the beloved preparing herself for the wedding;joy\ni would feel i missed out on a wealth of treasures if i did not read;sadness\ni finished the film i feel kind of regretful that i wasnt able to catch this on the big screen;sadness\ni feel like im caring about my body not in just an attempt to be the right size but to feel good and have a full life;love\ni feel so damaged i just want you to have care of me continuer;sadness\ni have found in the past when i blog daily i have more to say and i get out my feelings and emotions in more creative ways;joy\ni to candy factory it was clearly a tourist production line but it didn t feel unpleasant or hurried just well planned and professional an interesting and picturesque visit;sadness\ni feel that i m so pathetic and downright dumb to let people in let them toy with my feelings and then leaving me to clean up this pile of sadness inside me;sadness\ni am feeling very blessed today that they share such a close bond;joy\ni constantly feel these fits of discontent;sadness\nive been consumed by guilt and other feelings of discontent;sadness\ni feel like taking a whack at someone s eye and spitting on it a cranky old lady i try to cheer myself up;anger\ni feel really special and important;joy\ni sit the chicken preferably bone in chicken thighs skinless because i feel they have the most flavor in a crock pot so that it becomes tender and falls apart;love\ni feel empty and i wait for new signs;sadness\ni honestly do not feel discouraged today as i usually do;sadness\ni only feel such an aching rush if im hearing it;sadness\ni feel mmf and i cant be bothered to fight it;anger\ni cant sleep i switch on music if i need to wake up i switch on music if i feel morose music it is that comes to my rescue whenever i feel ecstatic the tunes are by my side if i want to meet my wild side hail music;sadness\ni feel so discontent with this decision;sadness\ni know it so difficult especially when you feel you have been wronged;anger\ni see the starlight caress your hair no more feel the tender kisses we used to share i close my eyes and clearly my heart remembers a thousand good byes could never put out the embers;love\ni hope i m proved wrong but i can t see the england u international hitting double figures next season and unless they invest in the rest of the team to provide him with service i feel they re doomed;sadness\ni could smell the chlorine feel my aching muscles see my portly mustached coach and prepubescent teammates and hear the whistles and hollers from the parents in the stands;sadness\ni have a feeling hes going to be way more successful than i am;joy\ni love this song and it always makes me feel happy;joy\ni everyone this will be a bit of a brief post as ive got a stinking cold at the moment and am feeling very very crappy but i have another page done on;sadness\ni feel a special draw toward and awed admiration for the firefighters who led the charge into the towers when everyone else was rushing out;joy\ni didn t feel accepted;joy\ni feel sometimes i am like heartless tin woodman sometimes like cowardly lion but i really want to believe there is a href http www;anger\ni am feeling like i am gonna blast;sadness"
feeling = ""
final = f"{pretext}\n{feeling};"
prediction = co.generate(
  model='large',
  prompt=final,
  max_tokens=50,
  temperature=0.75,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[" "],
  return_likelihoods='NONE')

# for rendering templates
# set up blueprint 
views = Blueprint('views', __name__)

# create routes (links to each page) and render html
@views.route('/', methods=['GET', 'POST']) # define view # not sure if post permission is needed
def home():   
  return render_template("home.html") # return to home page and render note

@views.route('/about')
def about():
  return render_template("about.html")

# should get user description as variable? # how to pass to NLP program? 
@views.route('/identify', methods=['GET', 'POST'])
def identify():
  return render_template("identify.html", thought=prediction.generations[0].text-final)

@views.route('/result')
def result():
  return render_template("result.html")

@views.route('/resources')
def resources():
  return render_template("resources.html")

@views.route('/guess-again')
def guess_again():
  return render_template("guessAgain.html")

@views.route('/login', methods=['GET', 'POST'])
def login():
  return render_template("login.html")
