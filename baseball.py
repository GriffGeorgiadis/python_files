#Griffin Georgiadis
#CS 21
#assignment 8
#Write a program that takes world series winners from a file and when a user
#enters a team, it displays the number of times they've won
#Start main
def main():
    #open File
    worldSeries_file = open('WorldSeriesWinners.txt','r')
    world_list = []
#strip \n
    for line in worldSeries_file.readlines():
        world_list.append(line.rstrip('\n'))




#list years
    years_list = []
    for i in range(len(world_list)):
        years = 1903 + i
        years_list.append(str(years))

    
    
    
#get inputs
    user_input = input("Enter baseball team:")
    file = []
    win = 0
    for index in range(len(world_list)):
        if user_input == world_list[index]:
            win += 1
            file.append(years_list[index])
        
        
                                    
            
#print results
    print("They won ",win,"times.")
    print('They won in the years: ',file)
    worldSeries_file.close()
            
        

main()
