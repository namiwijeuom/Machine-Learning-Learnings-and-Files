import google.generativeai as genai
import PIL.Image
import cv2 as cv

def check_API(API_KEY='AIzaSyDLyO2FtyO5F4pY2LmWnYN0rQgTDeDHqDs'):
    """Check if the API key is valid."""
    try:
        #API_KEY = 'AIzaSyDLyO2FtyO5F4pY2LmWnYN0rQgTDeDHqDs'
        genai.configure(api_key=API_KEY)
    except:
        print("Please check the API key.")
    
def take_snapshot_from_webcamera():
    """Take a snapshot from the webcamera."""

    # OpenCV will be used to capture an image from the webcam
    cap = cv.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    cap.set(3,640) #width=640
    cap.set(4,480) #height=480
    #ret,frame = cap.read() # return a single frame in variable `frame`

    while(True):

        ret,frame = cap.read() # return a single frame in variable `frame`
        cv.imshow('img1',frame) #display the captured image
        
        if cv.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
            cv.imwrite(r'C:\Users\Namina Wijetunga\Documents\Zone24x7\Images\c2.png',frame)
            cv.destroyAllWindows()
            break

    cap.release()

def save_and_open_image():
    """Save the image."""
    
    path_to_saved_image = r'C:\Users\Namina Wijetunga\Documents\Zone24x7\Images\c2.png'

    image = PIL.Image.open(path_to_saved_image)

    return image

def generate_content(image):
    """Generate content using the image."""

    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(image)

    return response.text

if __name__=='__main__':
    try:
        API_KEY = 'AIzaSyD10xVFJ0vpPJxS1RBg44OXQWZpK9GG_6'
        check_API(API_KEY)
        take_snapshot_from_webcamera()
        image = save_and_open_image()
        response = generate_content(image)
        print(response)

    except Exception as e:
        print(e)