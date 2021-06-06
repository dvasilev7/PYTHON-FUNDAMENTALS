#def update_version(version_list):
    #for num in range(len(int_version) - 1, -1, -1):
        #if int_version[num] < 9:
            #int_version[num] = int_version[num] + 1
            #break
        #else:
            #int_version[num] = 0


version = input().split(".")

new = f"{version[0]}{version[1]}{version[2]}"
new_num = str(int(new) + 1)

str_list = [num for num in new_num]
print(".".join(str_list))