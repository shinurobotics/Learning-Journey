ParticipantNumber = 5
ParticipantData = []
registeredParticipants = 0
OutputFile = open("ParticipantData.txt","w")

while (registeredParticipants < ParticipantNumber):
    tempPartData = [] #name,age,origin
    name = input("Please type your name:\n")
    tempPartData.append(name)
    age = int(input("Please type your age:\n"))
    tempPartData.append(age)
    country = input("Please type your origin country:\n")
    tempPartData.append(country)
    ParticipantData.append(tempPartData)
    registeredParticipants += 1
print(ParticipantData)

for participants in ParticipantData:
    for data in participants:
        OutputFile.write(str(data))
        OutputFile.write(" ")
    OutputFile.write("\n")
OutputFile.close()

InputFile = open("ParticipantData.txt","r")
InputList = []
for line in InputFile:
    tempParticipant = line.strip("\n").split()
    print(tempParticipant)
    InputList.append(tempParticipant)
    print(InputList)
     #strip() removes unnecessary space at beginning and end
     #title() make 1st letter of code capitalized
InputFile.close()

Age = {}
for part in InputList:
    tempAge = int(part[-1])
    if tempAge in Age:
            Age[tempAge] += 1
    else:
        Age[tempAge] = 1
print(Age)
