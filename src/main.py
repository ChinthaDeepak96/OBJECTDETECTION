from face_detection import detect_faces_in_video
from car_detection import detect_cars_in_video
from pedestrian_detection import detect_pedestrians_in_video

def main():
    print("Select detection type:")
    print("1. Faces")
    print("2. Cars")
    print("3. Pedestrians")
    choice = input("Enter choice (1-3): ")

    if choice == '1':
        detect_faces_in_video(0)  # 0 for webcam
    elif choice == '2':
        detect_cars_in_video(0)
    elif choice == '3':
        detect_pedestrians_in_video(0)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()