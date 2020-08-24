def count_letters(input_string):
    count_dict={}
    for s in input_string:
        if s not in count_dict.keys():
            count_dict[s]=1
        else:
            count_dict[s]+=1
    output_string1=str(count_dict.keys())
    output_string2=''
    for k,v in count_dict.items():
        output_string2=output_string2+k+str(v)
    return output_string1, output_string2
output_string1, output_string2=count_letters("aabcccdddd")
print(output_string1,output_string2)
