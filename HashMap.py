import sys

class Node:
    def __init__(self,key,val,next=None):
        self.key=key
        self.val=val
        self.next=next
def my_hash(s):
    h = 0
    for c in s:
        h = (h * 1_000_003 + ord(c)) % (2 ** 32)
    return h
class HashMap:
    def __init__(self,size=5):
        self.size=size
        self.buckets=size*[None]
        self.count=0
        self.fullBucket=0

    def expand(self):
        expanded=self.buckets.copy()
        self.buckets+=self.size*[None]
        self.size*=2
        for i in range(len(expanded)):
            n=expanded[i]
            while n:
                key,val=n.key,n.val
                self.remove(n.key,sizi=True)

                self.set(n.key,n.val,sizi=True)
                n=n.next

    def set(self,key,val=None,sizi=False):
        # if the key is not in map
        if self.contains(key,val,sizi)==False:
            self.count+=1

            hashed_key = my_hash(key.lower()) % self.size
            n=self.buckets[hashed_key]

            self.buckets[hashed_key] = Node(key, val, self.buckets[hashed_key])
            if n==None:
                self.fullBucket+=1
            if self.count/self.size>=4:
                self.expand()
                print(f'resizing to {self.size} buckets')
        else:
            hashed_key = my_hash(key.lower()) % self.size

            parent = None
            n = self.buckets[hashed_key]
            while n:
                if n.key.lower() == key.lower() and parent == None:
                    self.buckets[hashed_key].val=val

                elif n.key.lower() == key.lower():
                    parent.next.val=val
                parent = n
                n = n.next



    def contains(self, key,val=None,sizi=False):

        hashed_key = my_hash(key.lower()) % self.size



        n = self.buckets[hashed_key]
        while n:
            if n.key==key:
                return True

            n=n.next

        return False
    def get(self,key):

        hashed_key=my_hash(key.lower()) % self.size

        n=self.buckets[hashed_key]

        while n:
            if n.key==key:
                self.remove(key)

                return n.val
            n=n.next
        return None

    def remove(self,key,sizi=False):
        if sizi==False:
            hashed_key = my_hash(key) % self.size
        else:
            hashed_key = my_hash(key) % (self.size//2)

        parent=None
        n=self.buckets[hashed_key]
        while n:
            if n.key.lower()==key.lower():

                if parent ==None:
                    self.buckets[hashed_key]=self.buckets[hashed_key].next
                elif n.next!=None:
                    parent.next=n.next
                else:
                    parent.next=None
                self.count-=1
                break

            parent=n
            n=n.next

    def __repr__(self):
        s='----------------------------------------------------\n'
        for i in range(len(self.buckets)):
            n=self.buckets[i]
            s+=str(i)
            while n:
                s+='('+' '+n.key+' '+str(n.val)+')'
                n=n.next
            s+='\n'
        s+='----------------------------------------------------'
        return s
hMap=HashMap()


def makeWords(s):
    words=[]
    i=0
    while i<len(s):
        s1=''
        while i<len(s) and 'a'<=s[i].lower()<='z':
            s1+=s[i].lower()
            i+=1
        if s1!='':
            words.append(s1)
        i+=1
    return words



# input

while True:
    s=input()
    # end
    if s =='== END ==':
        break
    s=s.strip()
    s=makeWords(s)

    # adding words in map
    for i in range(len(s)):
        if hMap.contains(s[i]):
            val=hMap.get(s[i])
            hMap.set(s[i],val+1)
        else:
            hMap.set(s[i],1)
print('unique words = '+str(hMap.count))
for line in sys.stdin:
    val=hMap.get(line.strip())
    print(line.strip(),val)




