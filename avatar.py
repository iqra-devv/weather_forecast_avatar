import turtle


class Avatar:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=600, height=700)
        self.screen.bgcolor("light blue")
        self.screen.title("Recommended Outfit")
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.speed(0)
        self.pen.hideturtle()
        self.pen.width(3)

    def draw_head(self, x, y, radius):
        self.pen.goto(x, y - radius)
        self.pen.pendown()
        self.pen.fillcolor("peachpuff")
        self.pen.begin_fill()
        self.pen.circle(radius)
        self.pen.end_fill()
        self.pen.penup()

    def draw_eye(self, x, y, size):
        self.pen.goto(x, y)
        self.pen.down()
        self.pen.dot(size, "black")
        self.pen.up()

    def draw_nose(self, x, y, size):
        self.pen.goto(x, y)
        self.pen.down()
        self.pen.dot(size, "black")
        self.pen.up()

    def draw_mouth(self, x, y, length):
        self.pen.goto(x - length / 2, y)
        self.pen.pendown()
        self.pen.pencolor("black")
        self.pen.setheading(270)
        self.pen.circle(length / 2, 180)
        self.pen.penup()
        # draw body
    def draw_body(self, x, y, width, height):
        self.pen.goto(x - width / 2, y)
        self.pen.pendown()
        self.pen.fillcolor("peachpuff")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(width)
            self.pen.right(90)
            self.pen.forward(height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # draw arm
    def draw_arm(self, x, y, length, width):
        self.pen.goto(x, y)
        self.pen.pendown()
        self.pen.fillcolor("peachpuff")
        self.pen.begin_fill()
        self.pen.setheading(0)
        for _ in range(2):
            self.pen.forward(length)
            self.pen.right(90)
            self.pen.forward(width)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # draw legs
    def draw_legs(self, x, y, width, height):
        # Left leg
        self.pen.goto(x - width, y)
        self.pen.pendown()
        self.pen.fillcolor("peachpuff")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(width)
            self.pen.right(90)
            self.pen.forward(height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # Right leg
        self.pen.goto(x + 5, y)
        self.pen.pendown()
        self.pen.fillcolor("peachpuff")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(width)
            self.pen.right(90)
            self.pen.forward(height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # draw glove 
    def draw_glove(self, x, y, width, height):
        self.pen.goto(x, y)
        self.pen.pendown()
        self.pen.fillcolor("darkgray")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(width)
            self.pen.right(90)
            self.pen.forward(height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # draw shoe
    def draw_shoe(self, x, y, width, height):
        self.pen.goto(x, y)
        self.pen.pendown()
        self.pen.fillcolor("black")
        self.pen.begin_fill()
        self.pen.setheading(0)
        self.pen.forward(width)
        self.pen.right(90)
        self.pen.forward(height)
        self.pen.right(90)
        self.pen.forward(width + 10)
        self.pen.right(90)
        self.pen.forward(height)
        self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
    #draw cap 
    def draw_cap(self, x, y, radius):
        cap_radius = radius + 10
        self.pen.goto(x - cap_radius, y + radius + 10)
        self.pen.pendown()
        self.pen.fillcolor("gray")
        self.pen.begin_fill()
        self.pen.setheading(90)
        self.pen.circle(cap_radius, 180)
        self.pen.setheading(0)
        self.pen.forward(cap_radius * 2)
        self.pen.end_fill()
        self.pen.penup()
    # draw Tshirt
    def draw_tshirt(self, x, y, width, height, color="mediumseagreen"):
        # Draw main shirt body
        self.pen.goto(x - width / 2, y)
        self.pen.pendown()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(width)
            self.pen.right(90)
            self.pen.forward(height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # Draw left sleeve (half sleeve)
        sleeve_width, sleeve_height = 42, 40
        self.pen.goto(x - width / 2 - sleeve_width, y -20 )
        self.pen.pendown()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(sleeve_width)
            self.pen.right(90)
            self.pen.forward(sleeve_height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # Draw right sleeve (half sleeve)
        self.pen.goto(x + width / 2, y - 20)
        self.pen.pendown()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(sleeve_width)
            self.pen.right(90)
            self.pen.forward(sleeve_height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
 # draw Scarf
    def draw_scarf(self, x, y, width=40, height=120, color="crimson"):
        # Draw left scarf rectangle
        self.pen.goto(x - width // 2 - 20, y)
        self.pen.pendown()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(width)
            self.pen.right(90)
            self.pen.forward(height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # Draw right scarf rectangle
        self.pen.goto(x + width // 2 + 20, y)
        self.pen.pendown()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(width)
            self.pen.right(90)
            self.pen.forward(height-30)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
    # draw shorts
    def draw_shorts(self, x, y, width=130, height=200, color="navy"):
    
            # Draw left leg opening
        leg_width = 60
        leg_height = 80
        self.pen.goto(x - 70, y - 160 )
        self.pen.pendown()
        self.pen.fillcolor("navy")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(leg_width)
            self.pen.right(90)
            self.pen.forward(leg_height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
            # Draw right leg opening
        self.pen.goto(x - 5 , y - 160)
        self.pen.pendown()
        self.pen.fillcolor("navy")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(leg_width)
            self.pen.right(90)
            self.pen.forward(leg_height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()

    # draw pants
    def pants(self, x, y, width, height):
        # Left leg
        self.pen.goto(x - width, y)
        self.pen.pendown() 
        self.pen.fillcolor("steelblue")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(width)
            self.pen.right(90)
            self.pen.forward(height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # Right leg
        self.pen.goto(x + 5, y)
        self.pen.pendown()
        self.pen.fillcolor("steelblue")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(width)
            self.pen.right(90)
            self.pen.forward(height)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
    def jacket(self, x, y, width, height):
        # Draw main jacket body (rectangle over body)
        self.pen.goto(x - width / 2, y)
        self.pen.pendown()
        self.pen.fillcolor("firebrick")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(height)
            self.pen.right(90)
            self.pen.forward(width)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # Draw left sleeve attached to left arm
        sleeve_width, sleeve_height = 42, 100
        left_sleeve_x = x -225
        left_sleeve_y = y - 17 # move up to align with arm
        self.pen.goto(left_sleeve_x, left_sleeve_y)
        self.pen.pendown()
        self.pen.fillcolor("firebrick")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(sleeve_height)
            self.pen.right(90)
            self.pen.forward(sleeve_width)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()
        # Draw right sleeve attached to right arm
        right_sleeve_x = x + 75
        right_sleeve_y = y -17  # move up to align with arm
        self.pen.goto(right_sleeve_x, right_sleeve_y)
        self.pen.pendown()
        self.pen.fillcolor("firebrick")
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(sleeve_height)
            self.pen.right(90)
            self.pen.forward(sleeve_width)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()

        # draw character with optional wearables
    # def draw_character(self, shoes=False, gloves=False, cap=False , jacket=False, scarf=False, pants=False, tshirt=False, shorts=False):
    def draw_character(self, outfit_flags):
        head_x, head_y, head_radius = 0, 200, 60
        self.draw_head(head_x, head_y, head_radius)
      
        eye_y = head_y + 20
        self.draw_eye(head_x - 15, eye_y, 10)
        self.draw_eye(head_x + 15, eye_y, 10)
        self.draw_nose(head_x, head_y - 2, 5)
        self.draw_mouth(head_x, head_y - 15, 30)
        body_width, body_height = 250, 200
        body_x, body_y = head_x + 20, head_y - head_radius - 250
        self.draw_body(body_x, body_y, body_width, body_height)
        arm_length, arm_width = 100, 40
        self.draw_arm(body_x - body_width / 2 - arm_length, body_x + 100, arm_length, arm_width)
        self.draw_arm(body_x + 75, body_x + 100, arm_length, arm_width)
        leg_width, leg_height = 60, 180
        leg_y = body_y - 100
        self.draw_legs(body_x - 30, leg_y + 100, leg_width, leg_height)
        # Optionally draw gloves and shoes
        if outfit_flags["gloves"]:
            glove_width, glove_height = 25, 40
            self.draw_glove(body_x - 250, body_y + 230, glove_width, glove_height)
            self.draw_glove(body_x + 175, body_y + 230, glove_width, glove_height)
        if outfit_flags["shoes"]:
            shoe_width, shoe_height = 50, 20
            self.draw_shoe(body_x - 80, leg_y - 80, shoe_width, shoe_height)
            self.draw_shoe(body_x - 15, leg_y - 80, shoe_width, shoe_height)
        if outfit_flags["cap"]:
            self.draw_cap(head_x + 140, head_y - 40, head_radius)
        if outfit_flags["pants"]:
            self.pants(body_x - 30, leg_y + 100, leg_width, leg_height)
        if outfit_flags["jacket"]:
            self.jacket(body_x, body_y + 250 , body_width, body_height)
        if outfit_flags["scarf"]:
            self.draw_scarf(-20, 138, color="crimson")
        if outfit_flags["tshirt"]:
            self.draw_tshirt(-2, 139, 205, 250, color="mediumseagreen")
        if outfit_flags["shorts"]:
            self.draw_shorts(0, 50, width=130, height=70, color="navy")


    def stayopen(self):
        turtle.done()


if __name__ == "__main__":
    avatar = Avatar()
    avatar.draw_character()
    avatar.stayopen()