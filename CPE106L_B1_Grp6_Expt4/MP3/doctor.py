import random
import pickle

class Doctor():

    QUALIFIERS = ['Why do you say that ', 'You seem to think that ',
                  'Did I just hear you say that ', 'Why do you believe that ' ]

    REPLACEMENTS = {'I': 'you', 'me': 'you', 'my': 'your',
                    'we': 'you', 'us': 'you', 'am': 'are',
                    'you': 'I', 'You': 'I'}

    HEDGES = ['Go on.', 'I would like to hear more about that.',
              'And what do you think about this?', 'Please continue.']

    def __init__(self):
        self.history = []

        
        self.person = None

        
        self.firstTalk = True

        #dat file object
        #self.datFile = None

        #if dataisexisted already

    def greeting(self, client):
        
        return 'hello please state your name <>'
    def farewell(self):
        return 'Have a nice day!'

    def reply(self, sentence):
        '''
            yes all desrves a firstTalk
            search through data files
            if old , say welcome back 
                open it
                say + the last history
            else greetings
                create one
            if not firstTalk
            chat chat

            all convo reserves to history
            if disconnect save it
        '''
        answer = ''
        if self.firstTalk:
            self.person = str(sentence)
            #print(self.person)
            try:
                with open('users/'+self.person+'.dat', 'rb') as f:
                    self.history = pickle.load(f)
                    answer = 'Welcome Back ' +  \
                    self.person + \
                    ', Last Discussion: ' \
                    + str(self.history[-1]) 

            except Exception:
                #create one
                file = open('users/'+self.person+'.dat', 'x')
                file.close()
                answer = 'Greetings! ' + self.person

            finally:
                self.firstTalk = False
            #just dump the person
            return answer
        else:
            choice = random.randint (1, 10)
            if choice == 1:
                if len(self.history) > 3:
                    answer = 'Earlier you said that ' + \
                    self.change_person(random.choice(self.history))
                else:
                    answer = random.choice(Doctor.HEDGES)
            elif choice in (2,3,4,5):
                answer = random.choice(Doctor.QUALIFIERS) + \
                self.change_person(sentence)
            else:
                answer = random.choice(Doctor.HEDGES)
        self.history.append(answer)
        return answer
  
    def updateFile(self):
        '''it should update the open file then close. Should add more codes than close itself'''

        with open('users/'+self.person+'.dat', 'wb') as f:
            pickle.dump(self.history, f)

        
    def change_person(self, sentence):
        oldlist = sentence.split()
        newlist = []
        for word in oldlist:
            if word in Doctor.REPLACEMENTS:
                newlist.append(Doctor.REPLACEMENTS[word])
            else:
                newlist.append(word)
        return " ".join(newlist)
    
        
    



    
    
    

