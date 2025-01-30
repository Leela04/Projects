import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def canny_edge(img, low_threshold=50, high_threshold=150):
    return cv2.Canny(img, low_threshold, high_threshold)

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def gaussian_blur(img, kernel_size=5):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img):
    height = img.shape[0]
    polygons = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def hough_lines(img):
    return cv2.HoughLinesP(img, rho=2, theta=np.pi/180, threshold=100, 
                           minLineLength=40, maxLineGap=5)

def display_lines(img, lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image

def combine_images(original_img, line_img):
    return cv2.addWeighted(original_img, 0.8, line_img, 1, 1)

def detect_lane_lines(img):
    gray_img = grayscale(img)
    blur_img = gaussian_blur(gray_img)
    edges = canny_edge(blur_img)
    cropped_edges = region_of_interest(edges)
    lines = hough_lines(cropped_edges)
    line_img = display_lines(img, lines)
    final_img = combine_images(img, line_img)
    return final_img

def process_image(img_path):
    
    if not os.path.exists(img_path):
        print(f"Error: Image file {img_path} not found!")
        return

    img = cv2.imread(img_path)
    lane_image = detect_lane_lines(img)
    
    
    plt.imshow(cv2.cvtColor(lane_image, cv2.COLOR_BGR2RGB))
    plt.title("Lane Detection on Image")
    plt.show()

def process_video(video_path):
    
    if not os.path.exists(video_path):
        print(f"Error: Video file {video_path} not found!")
        return

    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Video file could not be opened.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame or end of video.")
            break

        
        lane_img = detect_lane_lines(frame)

        
        cv2.imshow("Lane Detection", lane_img)

        
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    mode = input("Enter the input sources (video or image)") 
    
    if mode == 'image':
        
        image_path = os.path.join('test_image.jpg')
        process_image(image_path)
        
    elif mode == 'video':
        
        video_path = os.path.join('test_video.mp4')
        process_video(video_path)

if __name__ == "__main__":
    main()

