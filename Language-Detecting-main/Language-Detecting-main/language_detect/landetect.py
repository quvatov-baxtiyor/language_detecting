from langdetect import detect

print(detect("bir iki üç"))
print(detect("one two three"))
print(detect("uno dos tres "))
print(detect("vienas du trys"))
print(detect("un deux trois"))
print(detect("en to tre"))
print(detect("isa Roa Telo"))

