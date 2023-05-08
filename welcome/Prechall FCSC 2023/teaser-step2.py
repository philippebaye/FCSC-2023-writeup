import cv2

image_in = cv2.imread('teaser.lsb-extraction.png')
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
good_fragments_order = [[(1, 5), (1, 2), (2, 0), (4, 7), (4,10)],
                        [(4, 1), (3, 7), (2, 4), (2, 7), (0,10)],
                        [(4, 3), (3, 4), (0, 2), (3, 0), (0, 1)],
                        [(3, 3), (0, 3), (3, 6), (2,10), (4, 9)], 
                        [(0, 5), (2, 8), (2, 6), (1, 4), (2, 2)],
                        [(0, 7), (4, 6), (0, 8), (4, 5), (0, 9)],
                        [(3,10), (0, 4), (4, 8), (4, 2), (2, 3)],
                        [(1, 9), (0, 0), (2, 5), (3, 8), (1, 0)], 
                        [(2, 9), (1, 1), (3, 2), (4, 4), (1, 8)], 
                        [(0, 6), (3, 5), (1, 6), (2, 1), (1, 3)], 
                        [(4, 0), (3, 9), (1,10), (1, 7), (3, 1)]]

# Recombinaison de l'image en positionnant les fragments à leurs bonnes places
for y in range(frag_count_in_height):
    for x in range(frag_count_in_width):
        bad_x, bad_y = good_fragments_order[y][x]
        set_fragment(image_out, x, y, get_fragment(image_in, bad_x, bad_y))

# Persistence de l'image recomposée
cv2.imwrite('teaser.lsb-extraction-recomposed.png', image_out)
