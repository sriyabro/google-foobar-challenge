def solution(s):
    cmap = {"z":43, "y":47, "x":45, "w":23, "v":57, "u":41, "t":30, "s":28, "r":58, "q":62, "p":60, "o":42, "n":46, "m":44, "l":56, "k":40, "j":22, "i":20, "h":50, "g":54, "f":52, "e":34, "d":38, "c":36, "b":48, "a":32}
    output = ""
    
    for char in  s:
        if char == " ":
            output += "000000"
        if char.isupper():
            output += "000001" + bin(cmap[char.lower()])[2:].zfill(6)
        if char in cmap:
            output += bin(cmap[char])[2:].zfill(6)
            

    print(output)




