import matplotlib.pyplot as plt

#diplay bar chart for progaraming popularility
def program():
    lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popular = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    print("Sample Data:")
    print("Languages: ",lang)
    print("Popularity: ",popular)
    plt.bar(lang,popular)
    plt.xlabel("Languagues")
    plt.ylabel("Popularity")
    plt.show()

#Diplay barchar Horizontal
def horizontal():
    lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popular = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    print("Sample Data:")
    print("Languages: ",lang)
    print("Popularity: ",popular)
    plt.barh(lang,popular)
    plt.xlabel("Languagues")
    plt.ylabel("Popularity")
    plt.show()

#bar chart using uniform color
def color():
    lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popular = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    print("Sample Data:")
    print("Languages: ",lang)
    print("Popularity: ",popular)
    plt.bar(lang,popular)
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.xlabel("Languagues")
    plt.ylabel("Popularity")
    plt.show()

#bar chart using diff color
def diffcolor():
    lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popular = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    print("Sample Data:")
    print("Languages: ",lang)
    print("Popularity: ",popular)
    plt.bar(lang,popular, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.xlabel("Languagues")
    plt.ylabel("Popularity")
    plt.show()    

#diplay bar chart with text label for each bar
def label():
    lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popular = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    #x_pos = [i for i, _ in enumerate(lang)]
    fig, ax = plt.subplots()
    rect = ax.bar(lang, popular)
    print("Sample Data:")
    print("Languages: ",lang)
    print("Popularity: ",popular)
    plt.bar(lang,popular)
    plt.xlabel("Languagues")
    plt.ylabel("Popularity")
    def autolabel(r):
        for rects in r:
            height = rects.get_height()
            ax.text(rects.get_x() + rects.get_width()/2., 1.05*height,
                    '%f' % float(height),
            ha='center', va='bottom')
    autolabel(rect)
    print(fig , ax)
    plt.show()

#accept user input options
io = input("1.vertical 2.horizontal 3.color 4.diffcolor 5.label Enter values:")

if io == "vertical":
    program()
elif io == "horizontal":
    horizontal()
elif io == "color":
    color()    
elif io == "diffcolor":
    diffcolor()
elif io == "label":
    label()
else: 
    print('Execute Success!!!')