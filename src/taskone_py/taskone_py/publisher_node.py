
import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne


class TaskOnePublisher(Node):
    def __init__(self):
        super().__init__('taskone_publisher')
        self.publisher = self.create_publisher(
            TaskOne, '/taskone', 10
        )

    def publish_input(self):
        try:
            ang_vel = float(input('Enter angular velocity (rad/s): '))
            radius = float(input('Enter wheel radius (m): '))

            if radius < 0:
                self.get_logger().error('Radius cannot be negative.')
                return

            msg = TaskOne()
            msg.ang_vel = ang_vel
            msg.radius = radius

            self.publisher.publish(msg)
            self.get_logger().info(
                f'Published: angular velocity={ang_vel}, '
                f'radius={radius}'
            )

        except ValueError:
            self.get_logger().error('Please enter valid numbers.')


def main(args=None):
    rclpy.init(args=args)
    node = TaskOnePublisher()

    try:
        while rclpy.ok():
            node.publish_input()
            rclpy.spin_once(node, timeout_sec=0.1)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
