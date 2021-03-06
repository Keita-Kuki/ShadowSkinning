import cv2

from lib.contour import find_contours_and_hierarchy, find_human_contour
from lib.triangulation import SimpleTriangulation

if __name__ == "__main__":
    src = cv2.imread("./images/shadow.jpg")
    dst = src.copy()
    contours, hierarchy = find_contours_and_hierarchy(src)
    human_contour = find_human_contour(contours, hierarchy)

    triangulation = SimpleTriangulation(src, human_contour)
    triangulation.draw_triangles(dst)

    # cv2.imwrite("./images/polygon_division.png", dst)
    cv2.imshow("mesh_division", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
