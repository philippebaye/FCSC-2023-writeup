import cv2

image_in = cv2.imread('teaser.png')
image_out = image_in.copy()

frag_count_in_height = 11
frag_count_in_width  = 5

frag_image_height = len(image_in) // frag_count_in_height
frag_image_width = len(image_in[0]) // frag_count_in_width


# Récupération des données d'un fragment
def get_fragment(image, x:int, y:int):
    frag_image_min_x = x * frag_image_width
    frag_image_max_x = (x+1) * frag_image_width
    frag_image_min_y = y * frag_image_height
    frag_image_max_y = (y+1) * frag_image_height
    return image[frag_image_min_y:frag_image_max_y, frag_image_min_x:frag_image_max_x]

# Mise à jour des données d'un fragment
def set_fragment(image, x:int, y:int, fragment):
    frag_image_min_x = x * frag_image_width
    frag_image_max_x = (x+1) * frag_image_width
    frag_image_min_y = y * frag_image_height
    frag_image_max_y = (y+1) * frag_image_height
    image[frag_image_min_y:frag_image_max_y, frag_image_min_x:frag_image_max_x] = fragment[:]

# La bonne position des différents fragments
good_fragments_order = [[(4, 7), (2, 7), (2, 6), (1, 7), (4, 4)],
                        [(1, 4), (0, 8), (0, 0), (3,10), (4, 9)],
                        [(1, 6), (1,10), (4,10), (1, 8), (2, 8)],
                        [(2, 1), (2, 2), (0, 2), (2, 0), (3, 8)], 
                        [(4, 5), (2, 4), (3, 9), (2, 9), (3, 7)],
                        [(2, 5), (3, 5), (3, 1), (4, 8), (0, 4)],
                        [(1, 5), (0, 9), (3, 2), (1, 3), (2,10)],
                        [(1, 2), (2, 3), (3, 4), (4, 6), (3, 6)],
                        [(4, 2), (3, 0), (3, 3), (0, 7), (0,10)],
                        [(1, 0), (4, 0), (0, 1), (4, 1), (0, 6)],
                        [(0, 5), (1, 9), (1, 1), (4, 3), (0, 3)]]

# Recombinaison de l'image en positionnant les fragments à leurs bonnes places
for y in range(frag_count_in_height):
    for x in range(frag_count_in_width):
        bad_x, bad_y = good_fragments_order[y][x]
        set_fragment(image_out, x, y, get_fragment(image_in, bad_x, bad_y))

# Persistence de l'image recomposée
cv2.imwrite('teaser-recomposed.png', image_out)
