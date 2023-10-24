import matplotlib.pyplot as plt

# Define the elements and their positions in the periodic table
elements = {
    "H":    (1,1),
    "He":   (19,1),
    "Li":	(1,2),
    "Be":	(2,2),
    "B":	(14,2),
    "C":	(15,2),
    "N":	(16,2),
    "O":	(17,2),
    "F":	(18,2),
    "Ne":	(19,2),
    "Na":	(1,3),
    "Mg":	(2,3),
    "Al":	(14,3),
    "Si":	(15,3),
    "P":	(16,3),
    "S":	(17,3),
    "Cl":	(18,3),
    "Ar":	(19,3),
    "K":	(1,4),
    "Ca":	(2,4),
    "Sc":	(3,4),
    "Ti":	(5,4),
    "V":	(6,4),
    "Cr":	(7,4),
    "Mn":	(8,4),
    "Fe":	(9,4),
    "Co":   (10,4),
    "Ni":   (11,4),
    "Cu":   (12,4),
    "Zn":   (13,4),
    "Ga":   (14,4),
    "Ge":   (15,4),
    "As":   (16,4),
    "Se":   (17,4),
    "Br":   (18,4),
    "Kr":   (19,4),
    "Rb":	(1,5),
    "Sr":   (2,5),
    "Y":    (3,5),
    "Zr":   (5,5),
    "Nb":   (6,5),
    "Mo":   (7,5),
    "Tc":   (8,5),
    "Ru":   (9,5),
    "Rh":   (10,5),
    "Pd":   (11,5),
    "Ag":   (12,5),
    "Cd":   (13,5),
    "In":   (14,5),
    "Sn":   (15,5),
    "Sb":   (16,5),
    "Te":   (17,5),
    "I":    (18,5),
    "Xe":   (19,5),
    "Cs":	(1,6),
    "Ba":	(2,6),
    "La":	(3,6),
    "Hf":	(5,6),
    "Ta":	(6,6),
    "W":	(7,6),
    "Re":	(8,6),
    "Os":	(9,6),
    "Ir":	(10,6),
    "Pt":	(11,6),
    "Au":	(12,6),
    "Hg":	(13,6),
    "Tl":	(14,6),
    "Pb":	(15,6),
    "Bi":	(16,6),
    "Po":	(17,6),
    "At":	(18,6),
    "Rn":	(19,6),
    "Fr":	(1,7),
    "Ra":	(2,7),
    "Ac":   (3,7),
    "Rf":	(5,7),
    "Db":	(6,7),
    "Sg":	(7,7),
    "Bh":	(8,7),
    "Hs":	(9,7),
    "Mt":	(10,7),
    "Ds":	(11,7),
    "Rg":	(12,7),
    "Cn":	(13,7),
    "Nh":	(14,7),
    "Fl":	(15,7),
    "Mc":	(16,7),
    "Lv":	(17,7),
    "Ts":	(18,7),
    "Og":	(19,7),
    "Ce":	(5,9),
    "Pr":	(6,9),
    "Nd":	(7,9),
    "Pm":	(8,9),
    "Sm":	(9,9),
    "Eu":	(10,9),
    "Gd":	(11,9),
    "Tb":	(12,9),
    "Dy":	(13,9),
    "Ho":	(14,9),
    "Er":	(15,9),
    "Tm":	(16,9),
    "Yb":	(17,9),
    "Lu":	(18,9),
    "Th":	(5,10),
    "Pa":	(6,10),
    "U":	(7,10),
    "Np":	(8,10),
    "Pu":	(9,10),
    "Am":	(10,10),
    "Cm":	(11,10),
    "Bk":	(12,10),
    "Cf":	(13,10),
    "Es":	(14,10),
    "Fm":	(15,10),
    "Md":	(16,10),
    "No":   (17,10),
    "Lr":	(18,10),
}

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

# Set axis limits
ax.set_xlim(0, 22)
ax.set_ylim(0, 12)

# Plot the periodic table
for symbol, (x, y) in elements.items():
    ax.text(x, y, symbol, fontsize=12, ha='center', va='center')
    ax.add_patch(plt.Rectangle((x - 0.5, y - 0.5), 1, 1, fill=False, edgecolor='black', linewidth=1))

# Set axis labels and title
ax.set_xlabel('Atomic Number', fontsize=14)
ax.set_ylabel('Period', fontsize=14)
ax.set_title('Periodic Table', fontsize=16, pad=20)

plt.gca().invert_yaxis()  # Invert the y-axis to match the conventional periodic table layout

# Ask the user to input an element
user_element = input("Enter an element symbol to place on the periodic table: ").strip()

# Check if the user's element is in the dictionary
if user_element in elements:
    x, y = elements[user_element]
    ax.text(x, y, user_element, fontsize=12, ha='center', va='center', color='red')

else:
    print(f"Element {user_element} not found in the periodic table.")

# Adding grid lines for clarity
plt.grid(True, linestyle='--', alpha=0.6)

# Adding a background color to the plot
ax.set_facecolor('#f4f4f4')

# Adding a frame around the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.show()
