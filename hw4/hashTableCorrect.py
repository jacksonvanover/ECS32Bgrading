class HashTableCorrect:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        # calculate hash value from key via hash function
        hashvalue = self.hashfunction(key,len(self.slots))

        # if the key isn't there already, add the entry
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # if the key is already there, update the entry
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            # if a different key is there, rehash until we find an empty slot or the key
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                    if nextslot == hashvalue:
                        print("RESIZING TABLE")

                        self.size = 2 * self.size + 1
                        i = 3
                        while i < self.size:
                            while self.size % i == 0:
                                self.size += 2
                            i+=1
                        
                        print("new size: ", self.size)

                        oldSlots = self.slots
                        oldData = self.data

                        self.slots = [None] * self.size
                        self.data = [None] * self.size

                        for i in range(0, len(oldSlots)):
                            if oldSlots[i]:
                                self.put(oldSlots[i],oldData[i])

                        return self.put(key,data)

                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data 

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)