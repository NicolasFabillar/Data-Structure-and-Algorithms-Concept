print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}')

import random
import string
import tkinter as tk
from tkinter import *

words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","acceptable","accessible","accidental","accurate","acid","acidic","acoustic","acrid","actually","ad hoc","adamant","adaptable","addicted","adhesive","adjoining","adorable","adventurous","afraid","aggressive","agonizing","agreeable","ahead","ajar","alcoholic","alert","alike","alive","alleged","alluring","aloof","amazing","ambiguous","ambitious","amuck","amused","amusing","ancient","angry","animated","annoyed","annoying","anxious","apathetic","aquatic","aromatic","arrogant","ashamed","aspiring","assorted","astonishing","attractive","auspicious","automatic","available","average","awake","aware","awesome","awful","axiomatic","bad","barbarous","bashful","bawdy","beautiful","befitting","belligerent","beneficial","bent","berserk","best","better","bewildered","big","billowy","bite-sized","bitter","bizarre","black","black-and-white","bloody","blue","blue-eyed","blushing","boiling","boorish","bored","boring","bouncy","boundless","brainy","brash","brave","brawny","breakable","breezy","brief","bright","bright","broad","broken","brown","bumpy","burly","bustling","busy","cagey","calculating","callous","calm","capable","capricious","careful","careless","caring","cautious","ceaseless","certain","changeable","charming","cheap","cheerful","chemical","chief","childlike","chilly","chivalrous","chubby","chunky","clammy","classy","clean","clear","clever","cloistered","cloudy","closed","clumsy","cluttered","coherent","cold","colorful","colossal","combative","comfortable","common","complete","complex","concerned","condemned","confused","conscious","cooing","cool","cooperative","coordinated","courageous","cowardly","crabby","craven","crazy","creepy","crooked","crowded","cruel","cuddly","cultured","cumbersome","curious","curly","curved","curvy","cut","cute","cute","cynical","daffy","daily","damaged","damaging","damp","dangerous","dapper","dark","dashing","dazzling","dead","deadpan","deafening","dear","debonair","decisive","decorous","deep","deeply","defeated","defective","defiant","delicate","delicious","delightful","demonic","delirious","dependent","depressed","deranged","descriptive","deserted","detailed","determined","devilish","didactic","different","difficult","diligent","direful","dirty","disagreeable","disastrous","discreet","disgusted","disgusting","disillusioned","dispensable","distinct","disturbed","divergent","dizzy","domineering","doubtful","drab","draconian","dramatic","dreary","drunk","dry","dull","dusty","dusty","dynamic","dysfunctional","eager","early","earsplitting","earthy","easy","eatable","economic","educated","efficacious","efficient","eight","elastic","elated","elderly","electric","elegant","elfin","elite","embarrassed","eminent","empty","enchanted","enchanting","encouraging","endurable","energetic","enormous","entertaining","enthusiastic","envious","equable","equal","erect","erratic","ethereal","evanescent","evasive","even","excellent","excited","exciting","exclusive","exotic","expensive","extra-large","extra-small","exuberant","exultant","fabulous","faded","faint","fair","faithful","fallacious","false","familiar","famous","fanatical","fancy","fantastic","far","far-flung","fascinated","fast","fat","faulty","fearful","fearless","feeble","feigned","female","fertile","festive","few","fierce","filthy","fine","finicky","first","five","fixed","flagrant","flaky","flashy","flat","flawless","flimsy","flippant","flowery","fluffy","fluttering","foamy","foolish","foregoing","forgetful","fortunate","four","frail","fragile","frantic","free","freezing","frequent","fresh","fretful","friendly","frightened","frightening","full","fumbling","functional","funny","furry","furtive","future","futuristic","fuzzy","gabby","gainful","gamy","gaping","garrulous","gaudy","general","gentle","giant","giddy","gifted","gigantic","glamorous","gleaming","glib","glistening","glorious","glossy","godly","good","goofy","gorgeous","graceful","grandiose","grateful","gratis","gray","greasy","great","greedy","green","grey","grieving","groovy","grotesque","grouchy","grubby","gruesome","grumpy","guarded","guiltless","gullible","gusty","guttural","habitual","half","hallowed","halting","handsome","handsomely","handy","hanging","hapless","happy","hard","hard-to-find","harmonious","harsh","hateful","heady","healthy","heartbreaking","heavenly","heavy","hellish","helpful","helpless","hesitant","hideous","high","highfalutin","high-pitched","hilarious","hissing","historical","holistic","hollow","homeless","homely","honorable","horrible","hospitable","hot","huge","hulking","humdrum","humorous","hungry","hurried","hurt","hushed","husky","hypnotic","hysterical","icky","icy","idiotic","ignorant","ill","illegal","ill-fated","ill-informed","illustrious","imaginary","immense","imminent","impartial","imperfect","impolite","important","imported","impossible","incandescent","incompetent","inconclusive","industrious","incredible","inexpensive","infamous","innate","innocent","inquisitive","insidious","instinctive","intelligent","interesting","internal","invincible","irate","irritating","itchy","jaded","jagged","jazzy","jealous","jittery","jobless","jolly","joyous","judicious","juicy","jumbled","jumpy","juvenile","kaput","keen","kind","kindhearted","kindly","knotty","knowing","knowledgeable","known","labored","lackadaisical","lacking","lame","lamentable","languid","large","last","late","laughable","lavish","lazy","lean","learned","left","legal","lethal","level","lewd","light","like","likeable","limping","literate","little","lively","lively","living","lonely","long","longing","long-term","loose","lopsided","loud","loutish","lovely","loving","low","lowly","lucky","ludicrous","lumpy","lush","luxuriant","lying","lyrical","macabre","macho","maddening","madly","magenta","magical","magnificent","majestic","makeshift","male","malicious","mammoth","maniacal","many","marked","massive","married","marvelous","material","materialistic","mature","mean","measly","meaty","medical","meek","mellow","melodic","melted","merciful","mere","messy","mighty","military","milky","mindless","miniature","minor","miscreant","misty","mixed","moaning","modern","moldy","momentous","motionless","mountainous","muddled","mundane","murky","mushy","mute","mysterious","naive","nappy","narrow","nasty","natural","naughty","nauseating","near","neat","nebulous","necessary","needless","needy","neighborly","nervous","new","next","nice","nifty","nimble","nine","nippy","noiseless","noisy","nonchalant","nondescript","nonstop","normal","nostalgic","nosy","noxious","null","numberless","numerous","nutritious","nutty","oafish","obedient","obeisant","obese","obnoxious","obscene","obsequious","observant","obsolete","obtainable","oceanic","odd","offbeat","old","old-fashioned","omniscient","one","onerous","open","opposite","optimal","orange","ordinary","organic","ossified","outgoing","outrageous","outstanding","oval","overconfident","overjoyed","overrated","overt","overwrought","painful","painstaking","pale","paltry","panicky","panoramic","parallel","parched","parsimonious","past","pastoral","pathetic","peaceful","penitent","perfect","periodic","permissible","perpetual","petite","petite","phobic","physical","picayune","pink","piquant","placid","plain","plant","plastic","plausible","pleasant","plucky","pointless","poised","polite","political","poor","possessive","possible","powerful","precious","premium","present","pretty","previous","pricey","prickly","private","probable","productive","profuse","protective","proud","psychedelic","psychotic","public","puffy","pumped","puny","purple","purring","pushy","puzzled","puzzling","quack","quaint","quarrelsome","questionable","quick","quickest","quiet","quirky","quixotic","quizzical","rabid","racial","ragged","rainy","rambunctious","rampant","rapid","rare","raspy","ratty","ready","real","rebel","receptive","recondite","red","redundant","reflective","regular","relieved","remarkable","reminiscent","repulsive","resolute","resonant","responsible","rhetorical","rich","right","righteous","rightful","rigid","ripe","ritzy","roasted","robust","romantic","roomy","rotten","rough","round","royal","ruddy","rude","rural","rustic","ruthless","sable","sad","safe","salty","same","sassy","satisfying","savory","scandalous","scarce","scared","scary","scattered","scientific","scintillating","scrawny","screeching","second","second-hand","secret","secretive","sedate","seemly","selective","selfish","separate","serious","shaggy","shaky","shallow","sharp","shiny","shivering","shocking","short","shrill","shut","shy","sick","silent","silent","silky","silly","simple","simplistic","sincere","six","skillful","skinny","sleepy","slim","slimy","slippery","sloppy","slow","small","smart","smelly","smiling","smoggy","smooth","sneaky","snobbish","snotty","soft","soggy","solid","somber","sophisticated","sordid","sore","sore","sour","sparkling","special","spectacular","spicy","spiffy","spiky","spiritual","spiteful","splendid","spooky","spotless","spotted","spotty","spurious","squalid","square","squealing","squeamish","staking","stale","standing","statuesque","steadfast","steady","steep","stereotyped","sticky","stiff","stimulating","stingy","stormy","straight","strange","striped","strong","stupendous","stupid","sturdy","subdued","subsequent","substantial","successful","succinct","sudden","sulky","super","superb","superficial","supreme","swanky","sweet","sweltering","swift","symptomatic","synonymous","taboo","tacit","tacky","talented","tall","tame","tan","tangible","tangy","tart","tasteful","tasteless","tasty","tawdry","tearful","tedious","teeny","teeny-tiny","telling","temporary","ten","tender","tense","tense","tenuous","terrible","terrific","tested","testy","thankful","therapeutic","thick","thin","thinkable","third","thirsty","thirsty","thoughtful","thoughtless","threatening","three","thundering","tidy","tight","tightfisted","tiny","tired","tiresome","toothsome","torpid","tough","towering","tranquil","trashy","tremendous","tricky","trite","troubled","truculent","true","truthful","two","typical","ubiquitous","ugliest","ugly","ultra","unable","unaccountable","unadvised","unarmed","unbecoming","unbiased","uncovered","understood","undesirable","unequal","unequaled","uneven","unhealthy","uninterested","unique","unkempt","unknown","unnatural","unruly","unsightly","unsuitable","untidy","unused","unusual","unwieldy","unwritten","upbeat","uppity","upset","uptight","used","useful","useless","utopian","utter","uttermost","vacuous","vagabond","vague","valuable","various","vast","vengeful","venomous","verdant","versed","victorious","vigorous","violent","violet","vivacious","voiceless","volatile","voracious","vulgar","wacky","waggish","waiting","wakeful","wandering","wanting","warlike","warm","wary","wasteful","watery","weak","wealthy","weary","well-groomed","well-made","well-off","well-to-do","wet","whimsical","whispering","white","whole","wholesale","wicked","wide","wide-eyed","wiggly","wild","willing","windy","wiry","wise","wistful","witty","woebegone","womanly","wonderful","wooden","woozy","workable","worried","worthless","wrathful","wretched","wrong","wry","yellow","yielding","young","youthful","yummy","zany","zealous","zesty","zippy","zonked","account","achiever","acoustics","act","action","activity","actor","addition","adjustment","advertisement","advice","aftermath","afternoon","afterthought","agreement","air","airplane","airport","alarm","amount","amusement","anger","angle","animal","ants","apparatus","apparel","appliance","approval","arch","argument","arithmetic","arm","army","art","attack","attraction","aunt","authority","babies","baby","back","badge","bag","bait","balance","ball","base","baseball","basin","basket","basketball","bat","bath","battle","bead","bear","bed","bedroom","beds","bee","beef","beginner","behavior","belief","believe","bell","bells","berry","bike","bikes","bird","birds","birth","birthday","bit","bite","blade","blood","blow","board","boat","bomb","bone","book","books","boot","border","bottle","boundary","box","boy","brake","branch","brass","breath","brick","bridge","brother","bubble","bucket","building","bulb","burst","bushes","business","butter","button","cabbage","cable","cactus","cake","cakes","calculator","calendar","camera","camp","can","cannon","canvas","cap","caption","car","card","care","carpenter","carriage","cars","cart","cast","cat","cats","cattle","cause","cave","celery","cellar","cemetery","cent","chalk","chance","change","channel","cheese","cherries","cherry","chess","chicken","chickens","children","chin","church","circle","clam","class","cloth","clover","club","coach","coal","coast","coat","cobweb","coil","collar","color","committee","company","comparison","competition","condition","connection","control","cook","copper","corn","cough","country","cover","cow","cows","crack","cracker","crate","crayon","cream","creator","creature","credit","crib","crime","crook","crow","crowd","crown","cub","cup","current","curtain","curve","cushion","dad","daughter","day","death","debt","decision","deer","degree","design","desire","desk","destruction","detail","development","digestion","dime","dinner","dinosaurs","direction","dirt","discovery","discussion","distance","distribution","division","dock","doctor","dog","dogs","doll","dolls","donkey","door","downtown","drain","drawer","dress","drink","driving","drop","duck","ducks","dust","ear","earth","earthquake","edge","education","effect","egg","eggnog","eggs","elbow","end","engine","error","event","example","exchange","existence","expansion","experience","expert","eye","eyes","face","fact","fairies","fall","fang","farm","fear","feeling","field","finger","finger","fire","fireman","fish","flag","flame","flavor","flesh","flight","flock","floor","flower","flowers","fly","fog","fold","food","foot","force","fork","form","fowl","frame","friction","friend","friends","frog","frogs","front","fruit","fuel","furniture","gate","geese","ghost","giants","giraffe","girl","girls","glass","glove","gold","government","governor","grade","grain","grandfather","grandmother","grape","grass","grip","ground","group","growth","guide","guitar","gun","hair","haircut","hall","hammer","hand","hands","harbor","harmony","hat","hate","head","health","heat","hill","history","hobbies","hole","holiday","home","honey","hook","hope","horn","horse","horses","hose","hospital","hot","hour","house","houses","humor","hydrant","ice","icicle","idea","impulse","income","increase","industry","ink","insect","instrument","insurance","interest","invention","iron","island","jail","jam","jar","jeans","jelly","jellyfish","jewel","join","judge","juice","jump","kettle","key","kick","kiss","kittens","kitty","knee","knife","knot","knowledge","laborer","lace","ladybug","lake","lamp","land","language","laugh","leather","leg","legs","letter","letters","lettuce","level","library","limit","line","linen","lip","liquid","loaf","lock","locket","look","loss","love","low","lumber","lunch","lunchroom","machine","magic","maid","mailbox","man","marble","mark","market","mask","mass","match","meal","measure","meat","meeting","memory","men","metal","mice","middle","milk","mind","mine","minister","mint","minute","mist","mitten","mom","money","monkey","month","moon","morning","mother","motion","mountain","mouth","move","muscle","name","nation","neck","need","needle","nerve","nest","night","noise","north","nose","note","notebook","number","nut","oatmeal","observation","ocean","offer","office","oil","orange","oranges","order","oven","page","pail","pan","pancake","paper","parcel","part","partner","party","passenger","payment","peace","pear","pen","pencil","person","pest","pet","pets","pickle","picture","pie","pies","pig","pigs","pin","pipe","pizzas","place","plane","planes","plant","plantation","plants","plastic","plate","play","playground","pleasure","plot","plough","pocket","point","poison","pollution","popcorn","porter","position","pot","potato","powder","power","price","produce","profit","property","prose","protest","pull","pump","punishment","purpose","push","quarter","quartz","queen","question","quicksand","quiet","quill","quilt","quince","quiver","rabbit","rabbits","rail","railway","rain","rainstorm","rake","range","rat","rate","ray","reaction","reading","reason","receipt","recess","record","regret","relation","religion","representative","request","respect","rest","reward","rhythm","rice","riddle","rifle","ring","rings","river","road","robin","rock","rod","roll","roof","room","root","rose","route","rub","rule","run","sack","sail","salt","sand","scale","scarecrow","scarf","scene","scent","school","science","scissors","screw","sea","seashore","seat","secretary","seed","selection","self","sense","servant","shade","shake","shame","shape","sheep","sheet","shelf","ship","shirt","shock","shoe","shoes","shop","show","side","sidewalk","sign","silk","silver","sink","sister","sisters","size","skate","skin","skirt","sky","slave","sleep","sleet","slip","slope","smash","smell","smile","smoke","snail","snails","snake","snakes","sneeze","snow","soap","society","sock","soda","sofa","son","song","songs","sort","sound","soup","space","spade","spark","spiders","sponge","spoon","spot","spring","spy","square","squirrel","stage","stamp","star","start","statement","station","steam","steel","stem","step","stew","stick","sticks","stitch","stocking","stomach","stone","stop","store","story","stove","stranger","straw","stream","street","stretch","string","structure","substance","sugar","suggestion","suit","summer","sun","support","surprise","sweater","swim","swing","system","table","tail","talk","tank","taste","tax","teaching","team","teeth","temper","tendency","tent","territory","test","texture","theory","thing","things","thought","thread","thrill","throat","throne","thumb","thunder","ticket","tiger","time","tin","title","toad","toe","toes","tomatoes","tongue","tooth","toothbrush","toothpaste","top","touch","town","toy","toys","trade","trail","train","trains","tramp","transport","tray","treatment","tree","trees","trick","trip","trouble","trousers","truck","trucks","tub","turkey","turn","twig","twist","umbrella","uncle","underwear","unit","use","vacation","value","van","vase","vegetable","veil","vein","verse","vessel","vest","view","visitor","voice","volcano","volleyball","voyage","walk","wall","war","wash","waste","watch","water","wave","waves","wax","way","wealth","weather","week","weight","wheel","whip","whistle","wilderness","wind","window","wine","wing","winter","wire","wish","woman","women","wood","wool","word","work","worm","wound","wren","wrench","wrist","writer","writing","yak","yam","yard","yarn","year","yoke","zebra","zephyr","zinc","zipper","zoo","accept","add","admire","admit","advise","afford","agree","alert","allow","amuse","analyse","announce","annoy","answer","apologise","appear","applaud","appreciate","approve","argue","arrange","arrest","arrive","ask","attach","attack","attempt","attend","attract","avoid","back","bake","balance","ban","bang","bare","bat","bathe","battle","beam","beg","behave","belong","bleach","bless","blind","blink","blot","blush","boast","boil","bolt","bomb","book","bore","borrow","bounce","bow","box","brake","branch","breathe","bruise","brush","bubble","bump","burn","bury","buzz","calculate","call","camp","care","carry","carve","cause","challenge","change","charge","chase","cheat","check","cheer","chew","choke","chop","claim","clap","clean","clear","clip","close","coach","coil","collect","colour","comb","command","communicate","compare","compete","complain","complete","concentrate","concern","confess","confuse","connect","consider","consist","contain","continue","copy","correct","cough","count","cover","crack","crash","crawl","cross","crush","cry","cure","curl","curve","cycle","dam","damage","dance","dare","decay","deceive","decide","decorate","delay","delight","deliver","depend","describe","desert","deserve","destroy","detect","develop","disagree","disappear","disapprove","disarm","discover","dislike","divide","double","doubt","drag","drain","dream","dress","drip","drop","drown","drum","dry","dust","earn","educate","embarrass","employ","empty","encourage","end","enjoy","enter","entertain","escape","examine","excite","excuse","exercise","exist","expand","expect","explain","explode","extend","face","fade","fail","fancy","fasten","fax","fear","fence","fetch","file","fill","film","fire","fit","fix","flap","flash","float","flood","flow","flower","fold","follow","fool","force","form","found","frame","frighten","fry","gather","gaze","glow","glue","grab","grate","grease","greet","grin","grip","groan","guarantee","guard","guess","guide","hammer","hand","handle","hang","happen","harass","harm","hate","haunt","head","heal","heap","heat","help","hook","hop","hope","hover","hug","hum","hunt","hurry","identify","ignore","imagine","impress","improve","include","increase","influence","inform","inject","injure","instruct","intend","interest","interfere","interrupt","introduce","invent","invite","irritate","itch","jail","jam","jog","join","joke","judge","juggle","jump","kick","kill","kiss","kneel","knit","knock","knot","label","land","last","laugh","launch","learn","level","license","lick","lie","lighten","like","list","listen","live","load","lock","long","look","love","man","manage","march","mark","marry","match","mate","matter","measure","meddle","melt","memorise","mend","mess up","milk","mine","miss","mix","moan","moor","mourn","move","muddle","mug","multiply","murder","nail","name","need","nest","nod","note","notice","number","obey","object","observe","obtain","occur","offend","offer","open","order","overflow","owe","own","pack","paddle","paint","park","part","pass","paste","pat","pause","peck","pedal","peel","peep","perform","permit","phone","pick","pinch","pine","place","plan","plant","play","please","plug","point","poke","polish","pop","possess","post","pour","practise","pray","preach","precede","prefer","prepare","present","preserve","press","pretend","prevent","prick","print","produce","program","promise","protect","provide","pull","pump","punch","puncture","punish","push","question","queue","race","radiate","rain","raise","reach","realise","receive","recognise","record","reduce","reflect","refuse","regret","reign","reject","rejoice","relax","release","rely","remain","remember","remind","remove","repair","repeat","replace","reply","report","reproduce","request","rescue","retire","return","rhyme","rinse","risk","rob","rock","roll","rot","rub","ruin","rule","rush","sack","sail","satisfy","save","saw","scare","scatter","scold","scorch","scrape","scratch","scream","screw","scribble","scrub","seal","search","separate","serve","settle","shade","share","shave","shelter","shiver","shock","shop","shrug","sigh","sign","signal","sin","sip","ski","skip","slap","slip","slow","smash","smell","smile","smoke","snatch","sneeze","sniff","snore","snow","soak","soothe","sound","spare","spark","sparkle","spell","spill","spoil","spot","spray","sprout","squash","squeak","squeal","squeeze","stain","stamp","stare","start","stay","steer","step","stir","stitch","stop","store","strap","strengthen","stretch","strip","stroke","stuff","subtract","succeed","suck","suffer","suggest","suit","supply","support","suppose","surprise","surround","suspect","suspend","switch","talk","tame","tap","taste","tease","telephone","tempt","terrify","test","thank","thaw","tick","tickle","tie","time","tip","tire","touch","tour","tow","trace","trade","train","transport","trap","travel","treat","tremble","trick","trip","trot","trouble","trust","try","tug","tumble","turn","twist","type","undress","unfasten","unite","unlock","unpack","untidy","use","vanish","visit","wail","wait","walk","wander","want","warm","warn","wash","waste","watch","water","wave","weigh","welcome","whine","whip","whirl","whisper","whistle","wink","wipe","wish","wobble","wonder","work","worry","wrap","wreck","wrestle","wriggle","x-ray","yawn","yell","zip","zoom"]

top = tk.Tk()
top.title("Word Guessing Game")
top.geometry("850x705")
top.configure(bg = "#AEC6CF")

word = random.choice(words).upper()

while "-" in word or " " in word:
    word = random.choice(words).upper()

LettersInWord = list(word.upper())
LettersInWord = [i for n, i in enumerate(LettersInWord) if i not in LettersInWord[:n]]
Alphabet = list(string.ascii_uppercase)
UsedLetters = list()

print(LettersInWord)

lives = 5
Hints = 3
WordGuessed = 0
GameStarter = 0

def PlayAgain():
    global WordGuessed
    global word
    global words
    global LettersInWord
    global UsedLetters
    global lives
    global Hints
    global GameStarter

    if not LettersInWord or GameStarter == 1:
        word = random.choice(words).upper()

        while "-" in word or " " in word:
            word = random.choice(words).upper()

        LettersInWord = list(word.upper())
        LettersInWord = [i for n, i in enumerate(LettersInWord) if i not in LettersInWord[:n]]
        UsedLetters = []
        lives = 5
        Hints = 3
        Value5.set(' '.join(UsedLetters))
        Value1.set(' '.join(CurrentWord()))
        Value2.set(lives)
        Value3.set(Hints)
        Value6.set("New Game! New Word to Guess!")
        ChangeGreetings()
        print(LettersInWord)

    else:
        Value6.set("Guess the word first!")

    GameStarter = 0

def CurrentWord():
    WordDisplay = list()
    for Letter in word:
        if Letter in UsedLetters:
            WordDisplay.append(Letter)
        else:
            WordDisplay.append("-")
    return WordDisplay

def PlayGame():
    global WordGuessed
    global lives
    UserInput = LetterInput.get().upper()
    if len(LettersInWord) != 0 and lives != 0:
        if UserInput in UsedLetters:
            Value6.set("You already chose that letter. Choose a different one. ")

        elif UserInput in Alphabet and UserInput not in UsedLetters:
            UsedLetters.append(UserInput)
            if UserInput in LettersInWord:
                for Letter in LettersInWord:
                    if UserInput == Letter:
                        LettersInWord.remove(Letter)

                Value6.set("Good Job!")
            else:
                Value6.set("Wrong Guess!")
                lives -= 1

        if not UserInput:
            Value6.set("Enter a letter in the box first.")

    if len(LettersInWord) == 0:
        Value6.set("BINGO! The word is: " + word)
        WordGuessed += 1
        top.after(2000, PlayAgain)

    if lives == 0:
        Value6.set("Game Over! You got no more life. The word is: " + word)
        WordGuessed = 0

    Value1.set(' '.join(CurrentWord()))
    Value2.set(lives)
    Value5.set(' '.join(UsedLetters))
    Value7.set(WordGuessed)
    LetterInput.set("")
    ChangeGreetings()

def Hint():
    global Hints
    global WordGuessed
    if Hints > 0:
        FreeLetter = random.choice(LettersInWord)
        UsedLetters.append(FreeLetter)
        for Letter in LettersInWord:
            if FreeLetter == Letter:
                LettersInWord.remove(Letter)

        Hints -= 1
        if len(LettersInWord) != 0:
            Value6.set("Hint Given!")

    if Hints == 0:
        if len(LettersInWord) != 0:
            Value6.set("No more tips left.")

    if len(LettersInWord) == 0:
        Value6.set("BINGO! The word is: " + word)
        WordGuessed += 1
        top.after(2000, PlayAgain)

    Value1.set(' '.join(CurrentWord()))
    Value3.set(Hints)
    Value5.set(' '.join(UsedLetters))
    Value7.set(WordGuessed)
    ChangeGreetings()

def GiveUp():
    global WordGuessed
    global GameStarter
    WordGuessed = 0
    Value6.set("You Failed! The word is: " + word)
    GameStarter = 1
    top.after(2000, PlayAgain)

def ChangeGreetings():
    global WordGuessed
    if WordGuessed == 0:
        Label0.config(text="Welcome to word guessing game! ")
    if WordGuessed == 1:
        Label0.config(text = "Great! But can you guess 5 words?")
    if WordGuessed == 5:
        Label0.config(text = "Wow! But I bet you can't guess 10 words.")
    if WordGuessed == 10:
        Label0.config(text = "OMG! Who was I to doubt you.")
    if WordGuessed == 11:
        Label0.config(text="But, my best was 16 ;)")

Label0 = Label(top, text = "Welcome to word guessing game! ", bg = "#AEC6CF",font=("Comic Sans MS", 25, "bold"), width = 40)
Label0.place(x = 30, y = 26)

Value1 = StringVar()
Value1.set(' '.join(CurrentWord()))
Value2 = StringVar()
Value2.set(lives)
Value3 = StringVar()
Value3.set(Hints)
Value7 = StringVar()
Value7.set(WordGuessed)

Label1 = Label(top, text = "Lives:", bg = "#9cc1d0", font=("Comic Sans MS", 20, "bold")).place(x = 40, y = 120)
Label1a = tk.Entry(top, width = 10, state = "disable", textvariable = Value2,justify = CENTER, font=("Comic Sans MS", 20, "bold")).place(x = 160, y = 120)
Label2 = Label(top, text = "Hints: ", bg = "#9cc1d0", font=("Comic Sans MS", 20, "bold")).place(x = 40, y = 200)
Label2a = tk.Entry(top, width = 10, state = "disable", textvariable = Value3,justify = CENTER, font=("Comic Sans MS", 20, "bold")).place(x = 160, y = 200)
Label7 = Label(top, text = "Word Guessed:", bg = "#9cc1d0", font=("Comic Sans MS", 22, "bold")).place(x = 380, y = 150)
Label7a = tk.Entry(top, width = 10, state = "disable", textvariable = Value7,justify = CENTER, font=("Comic Sans MS", 22, "bold")).place(x = 630, y = 150)

Value6 = StringVar()
Value6.set("New Game")
Label6 = tk.Entry(top, state = "disable", width = 50, textvariable = Value6,justify = CENTER, font=("Comic Sans MS", 20, "bold") ).place(x = 20, y = 290)

Value5 = StringVar()
Label5 = Label(top, text = "Used Letters: ", bg = "#9cc1d0",font=("Comic Sans MS", 20, "bold")).place(x = 40, y = 380)
Label5a = tk.Entry(top, state = "disable", textvariable = Value5,justify = CENTER,font=("Comic Sans MS", 20, "bold")).place(x = 300, y = 380)


Label3 = Label(top, text = "Word To Guess: ", bg = "#9cc1d0",font=("Comic Sans MS", 20, "bold")).place(x = 40, y = 470)
Label3a = tk.Entry(top, state = "disable", textvariable = Value1,justify = CENTER,font=("Comic Sans MS", 20, "bold")).place(x = 300, y = 470)

Label4 = Label(top, text = "Input a letter:", bg = "#9cc1d0",font=("Comic Sans MS", 20, "bold")).place(x = 40, y = 550)
LetterInput = StringVar()
InputBox1 = Entry(top, textvariable = LetterInput,bg = "#FAC898", justify = CENTER,font=("Comic Sans MS", 20, "bold")).place(x = 300, y = 550)
Enter = Button(top,width = 11, text = "ENTER", activebackground = "white", command = PlayGame,bg = "#FAC898",font=("Comic Sans MS", 15, "bold"))
Enter.place(x = 670, y = 545)

HintButton = Button(top,width = 11, text = "Hint", activebackground = "white", command = Hint,bg = "#779ECB",font=("Comic Sans MS", 15, "bold")).place(x = 670, y = 465)
PlayAgainButton = Button(top,width = 11, text = "Continue", activebackground = "white", command = PlayAgain,bg = "#779ECB",font=("Comic Sans MS", 15, "bold")).place(x = 670, y = 375)
GiveUpButton = Button(top,width = 11, text = "Give Up", activebackground = "white", command = GiveUp,bg = "#779ECB",font=("Comic Sans MS", 15, "bold")).place(x = 390, y = 625)

top.mainloop()