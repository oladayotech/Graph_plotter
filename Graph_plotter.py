# import library
import matplotlib.pyplot as plt
import numpy as np

# dictionary for the graph
graph_category = {"1":"line graph", "2":"scatter plot", "3":"bar chart", "4":"horizontal bar chart", "5":"histogram", "6":"pie chart \n"}

def display_graph_display():
   # Displays types of graph this program can create using the dictonary above, graph_category
   for index, values in graph_category.items():
      # Prints graph categories
      print(f"Enter {index} for {values}")

display_graph_display()

# Used to select the type of graph
def graph_selector():
   # Iteration till a condition is met, 
   # when user input right data type
   while True:
      # Error handling
      try:
         # Get user input
         user_input = int(input("Enter an integer to match the above: "))

         # Check if user input meets requirement,
         # between 1 and 6
         if user_input >= 1 and user_input <= 6:
            # Once met return the result for computation
            return user_input
         else:
            # if condition is not met, print the below
            print("Please input an integer value between 1 and 6")
      except:
            print("Please input a valid integer")

user_input = graph_selector()

def graph_generation():
   # used to generate graph
   def line_graph():
      try:
         
         # Checks if the user selected line graph
         if user_input == 1:

            # Gets user input
            x_axis_line_graph = np.array(list(input("\nEnter an array1 to create a line graph: ")))
            y_axis_line_graph = np.array(list(input("Enter an array2 to create a line graph: ")))

            # Create line graph
            plt.plot(x_axis_line_graph, y_axis_line_graph, marker = 'o', linestyle = '--', color='black')

            # Set the title
            plt.title("Line graph")

            # Set the labels for the x and y axes
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')

            # Displays line graph
            plt.show()
      except ValueError:
         print("Values must have same dimensions")

   def scatter_plot():
      try:
         if user_input == 2:

            # Get input from user
            x_axis_scatter_plot = np.array(list(input("\nEnter an array1 to create a scatter plot: ")))
            y_axis_scatter_plot = np.array(list(input("Enter an array2 to create a scatter plot: ")))

            # Create Scatter plot
            plt.scatter(x_axis_scatter_plot, y_axis_scatter_plot, color='red', marker='o', s=100, edgecolors='black')

            # Set the title
            plt.title("Scater plot")

            # Set the labels for the x and y axes
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')

            # Displays the scatter plot
            plt.show()
      except:
         print("x and y must be the same size")

   def bar_chart():
      # Creates a bar chart based on user input.
      
      # Check if the user selected the bar chart option
      if user_input == 3:
        
        # Get the categories from the user
        category_bar_chart = input("\nInput categories (comma-separated): ")
        
        # Split the input string into a list of categories
        # and remove any leading or trailing whitespace
        categories = [category.strip() for category in category_bar_chart.split(",")]
        
        # Get the values from the user
        values = input("Enter values (comma-separated): ")
        
        # Try to convert the input values to a list of floats
        try:
            values = [float(value) for value in values.split(",")]
        
        # If the conversion fails, print an error message and return
        except ValueError:
            print("Error: Values must be numeric.")
            return
        
        # Check if the number of categories and values match
        if len(categories) != len(values):
            print("Error: Number of categories and values must match.")
            return
        
        # Create the bar chart
        plt.bar(categories, values, color=['orange','pink','skyblue','gray'], edgecolor='red')

        # Set the title of the chart
        plt.title("Bar chart")
        
        # Set the labels for the x and y axes
        plt.xlabel('Categories')
        plt.ylabel('Values')
        
        # Display the chart
        plt.show()

   def horizontal_bar_chart():
      # Creates a bar chart based on user input.
      
      # Check if the user selected the bar chart option
      if user_input == 4:
        
        # Get the categories from the user
        category_horizontal_bar_chart = input("\nInput categories (comma-separated): ")
        
        # Split the input string into a list of categories
        # and remove any leading or trailing whitespace
        categories = [category.strip() for category in category_horizontal_bar_chart.split(",")]
        
        # Get the values from the user
        values = input("Enter values (comma-separated): ")
        
        # Try to convert the input values to a list of floats
        try:
            values = [float(value) for value in values.split(",")]
        
        # If the conversion fails, print an error message and return
        except ValueError:
            print("Error: Values must be numeric.")
            return
        
        # Check if the number of categories and values match
        if len(categories) != len(values):
            print("Error: Number of categories and values must match.")
            return
        
        # Create the horizontal bar chart
        plt.barh(categories, values, color=['orange','pink','skyblue','gray'], edgecolor='red')

        # Set the title of the chart
        plt.title("Horizontal Bar chart")
        
        # Set the labels for the x and y axes
        plt.xlabel('Categories')
        plt.ylabel('Values')
        
        # Display the chart
        plt.show()

   def histogram():
      # Checks if the input is the selected input is for histogram
      if user_input == 5:
         values = list(input("\nEnter an array to create an histogram: "))
         # Create histogram
         plt.hist(values, bins=5, color='skyblue', edgecolor='black')

         # Set tittle of the graph
         plt.title("Histogram")

         # Set the labels for the x and y axes
         plt.xlabel('Values')
         plt.ylabel('Frequency')

         # Display the graph
         plt.show()

   def pie_chart():

   #    # Checks if the input is the selected input is for pie chart

      if user_input == 6:
        values = input("\nEnter values (comma-separated): ")

        # Try to convert the input values to a list of floats
        try:
            values = [float(value) for value in values.split(",")]
        except ValueError:
            print("Error: Values must be numeric.")
            return
        
         # get input from user  
        labels = input("Enter labels (comma-separated): ")
        labels = [label.strip() for label in labels.split(",")]

        # Check if the number of categories and values match
        if len(labels) != len(values):
            print("Error: Number of categories and values must match.")
            return
        
        plt.pie(values, labels=labels, startangle=90)

        # Set title of chart  
        plt.title("Pie Chart")

      #   Displays the chart
        plt.show()

   # Calling of functions
   line_graph()
   scatter_plot()
   bar_chart()
   horizontal_bar_chart()
   histogram()
   pie_chart()

graph_generation()

# Used for plotting more graph
def replay_button():
   # Ask the user if they wanna plot more graph
   print(" \nDo you want to plot more graph")
   user_input_8 = input("Type (N) for No and (Y) for Yes: ")

   # Checks if user wanna keep playing
   if user_input_8.lower() == "y":

      # Recall functions
      display_graph_display()
      graph_selector()
      graph_generation()
      replay_button()
   else:
      print("Have lovely day")
replay_button()