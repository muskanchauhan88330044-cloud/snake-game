
import cv2
import pygame
import threading
import time
from gesture_controller import GestureController
from snake_game import SnakeGame


class GameManager:
    def __init__(self):
        pygame.init()  # ✅ Initialize pygame properly

        self.game = SnakeGame()
        self.gesture_controller = GestureController()
        self.cap = None
        self.running = True
        self.gesture_thread = None

        # Gesture state
        self.current_gesture = None
        self.is_speed_boost = False

    def initialize_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open webcam")
            return False

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        return True

    def gesture_detection_loop(self):
        while self.running and self.cap is not None:
            ret, frame = self.cap.read()
            if not ret:
                continue

            frame = cv2.flip(frame, 1)

            gesture, pinch, annotated_frame = self.gesture_controller.detect_gestures(frame)

            self.current_gesture = gesture
            self.is_speed_boost = pinch

            cv2.imshow('Nokia Snake - Gesture Control', annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False
                break

            time.sleep(0.033)

    def run(self):
        if not self.initialize_camera():
            print("Failed to initialize camera. Exiting...")
            return

        # Start gesture thread
        self.gesture_thread = threading.Thread(target=self.gesture_detection_loop)
        self.gesture_thread.daemon = True
        self.gesture_thread.start()

        print("Nokia Snake Game Started!")

        last_update = time.time()

        while self.running:
            current_time = time.time()

            # Handle pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # Gesture controls
            if self.current_gesture:
                self.game.change_direction(self.current_gesture)
                if self.game.game_over:
                    self.game.handle_restart(self.current_gesture)

            # Speed boost
            self.game.set_speed_boost(self.is_speed_boost)

            # Game update
            target_fps = self.game.get_current_speed()
            if current_time - last_update >= 1.0 / target_fps:
                self.game.update()
                last_update = current_time

            # Draw game
            self.game.draw()
            self.game.clock.tick(60)

        self.cleanup()

    def cleanup(self):
        print("Cleaning up...")
        self.running = False

        if self.cap is not None:
            self.cap.release()

        cv2.destroyAllWindows()
        pygame.quit()  # ✅ Important fix

        if self.gesture_thread and self.gesture_thread.is_alive():
            self.gesture_thread.join(timeout=1.0)

        print("Game closed successfully!")


def main():
    try:
        game_manager = GameManager()
        game_manager.run()
    except KeyboardInterrupt:
        print("\nGame interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()


