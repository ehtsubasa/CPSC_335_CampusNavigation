
import tkinter as tk
from tkinter import Canvas, Frame, Entry, messagebox

import networkx as nx

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.artist import Artist

from data import *


#================#
#   Functions    #
#================#
# Breadth-first search function to find the shortest path between two nodes
# Input:  Graph(nx.graph), start(int), end(int)
# Output: List of nodes that form the shortest path
def bfs_shortest_path(graph, start, end):
    visited = {start}
    queue = [(start, [start])]    #ex: (3, [0,1,3])

    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                if neighbor == end:
                    return path + [neighbor] 
                else:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
    return None  # Return None if no path is found



# Function to perform Depth-First Search and find all possible paths between two nodes,
# then checking if the path passes through all required nodes.
# Input:  Graph(nx.graph), start(int), end(int), required_nodes(int)
# Output: List of path (list of list(int))
def dfs_all_paths(graph, start, end, required_nodes, max_depth=15):
    # Initialize stack with the starting node and path
    stack = [(start, [start])]
    found_paths = []
    required_nodes = set(required_nodes)  # Ensure required_nodes is a set for fast lookup

    while stack and len(found_paths) < 5:
        (current_node, path) = stack.pop()
        
        # Stop if the path length exceeds max_depth
        if len(path) > max_depth:
            continue          

        # If we reach the goal and the path includes all required nodes, save the path
        if current_node == end and required_nodes.issubset(path):
            found_paths.append(path)
            continue  # Continue to look for more paths

        # Explore neighbors of the current node
        for neighbor in graph.neighbors(current_node):
            if neighbor not in path:  # Avoid cycles by ensuring no revisits
                stack.append((neighbor, path + [neighbor]))

    return found_paths   


# Function to perform Dijkstra's algo and find shortest 
# path between two nodes based on weight
# Input:  Graph(nx.graph), start(int), end(int)
# Output: List of nodes that form the shortest path
def dijkstra_shortest_path(graph, start, end):
    try:
        # Use NetworkX's dijkstra_path to find the shortest path by weight
        path = nx.dijkstra_path(graph, source=start, target=end, weight='weight')
        total_weight = nx.dijkstra_path_length(graph, start, end, weight='weight')
        return path, total_weight
    except nx.NetworkXNoPath:
        messagebox.showerror("Error", "No path found.")
        return None    



#====================#
#   Class for GUI    #
#====================#
class GUI:
    def __init__(self, root):
        self.root = root 
        self.root.title("Campus Navigation App")
        self.root.geometry("1100x1000")
        self.root.configure(bg='white') 
        
        self.disabled_nodes = set()
        self.disabled_edges = set()
        self.req_nodes = []
        
        self.index = 0
        self.all_paths = []
        self.setup_gui()    
        
 
        
    #  Create GUI layout
    #===========================
    def setup_gui(self):
        left_frame = tk.Frame(root, width=300, height=1000, bg='white')
        left_frame.pack(side="left", fill="both", expand=True, padx=(40,0), pady=50)    
            
            
        #input field Start Node
        tk.Label(left_frame, text="Start:", bg='white', fg='black', 
                 font=('Times New Roman', 20)).grid(row=0, column=0, padx=(40,0))
        self.start_node_entry = tk.Entry(left_frame, width=13, bg='gray', highlightthickness=0)
        self.start_node_entry.grid(row=0, column=1, padx=(0,10), sticky='W')
            
        #input field End Node
        tk.Label(left_frame, text="Destination:", bg='white', fg='black', 
                 font=('Times New Roman', 20)).grid(row=1, column=0, padx=(40,0))
        self.end_node_entry = tk.Entry(left_frame, width=13, bg='gray', highlightthickness=0)
        self.end_node_entry.grid(row=1, column=1, padx=(0,10), sticky='W')
         
        #input field Required Node
        tk.Label(left_frame, text="Add stops:", bg='white', fg='black', 
                 font=('Times New Roman', 20)).grid(row=2, column=0, padx=(40,0))
        self.req_entry = tk.Entry(left_frame, width=13, bg='gray', highlightthickness=0)
        self.req_entry.grid(row=2, column=1, padx=(0,10), sticky='W')         
           
        #Button to display BFS
        tk.Button(left_frame, text="Run BFS", command=self.bfs, 
                  background='lightgray', highlightbackground="white", 
                  height=2, width=20).grid(row=3, column=0, columnspan=2, pady=(50,5))
        
            
        #Button to display DFS
        tk.Button(left_frame, text="Run DFS", command=self.dfs, 
                  background='lightgray', highlightbackground="white", 
                  height=2, width=20).grid(row=4, column=0, columnspan=2, pady=5)
            
        #Button to start the Djstrika's algo
        tk.Button(left_frame, text="Run Dijkstra's", command=self.dijkstra, 
                  background='lightgray', highlightbackground="white", 
                  height=2, width=20).grid(row=5, column=0, columnspan=2, pady=5)
            
        
        #"Next" button to show the next path in the list of found paths (DFS only)
        self.next_button = tk.Button(left_frame, text="Next", command=self.show_next_path, 
                                background='lightgray', highlightbackground="white", state=tk.DISABLED)
        self.next_button.grid(row=6, column=2, pady=(20,0), sticky='SW')  
        
        #"Prev" button to show the next path in the list of found paths (DFS only)
        self.prev_button = tk.Button(left_frame, text="Prev", command=self.show_prev_path, 
                                background='lightgray', highlightbackground="white", state=tk.DISABLED)
        self.prev_button.grid(row=6, column=1, pady=(20,0), sticky='SE')          
        
        # Button to reset the graph to its original state
        tk.Button(left_frame, text="Reset", command=self.reset_graph, 
                  background='lightgray', highlightbackground="white").grid(row=6, column=1, pady=(20,0), sticky='SW')       
        
        #Button to remove nodes and redraw the graph
        tk.Button(left_frame, text="Add", command=self.check_and_get_req, 
                  background='lightgray', highlightbackground="white").grid(row=2, column=2, sticky='W')
        
        #Label for dispaly distance
        self.distance_label = tk.Label(left_frame, text=" ", bg='white', fg='black', 
                 font=('Times New Roman', 16, 'italic'))
        self.distance_label.place(relx=0.3, rely=0.92)
        #self.distance_label.grid(row=7, stick='S')        
            
        #Create a canvas to display the graph using Matplot
        right_frame = tk.Frame(root, width=600, height=1000)
        right_frame.pack(side="right", fill="both", expand=True)    
        self.canvas = tk.Canvas(right_frame, width=600, height=800)
        self.canvas.pack(fill="both", expand=True)
        
        # Draw the graph on the canvas
        self.draw_graph(path=[])  
              

        
    # Method for checking user input  
    #===============================
    def check_input(self):
        start_node = self.start_node_entry.get().strip()
        end_node = self.end_node_entry.get().strip()    
        global location_names
        
        #Check for valid input
        if not start_node or not end_node:
            messagebox.showerror("Error", "Please enter the valid start and end node with relevent weight.")
            return
        
        try:
            start_node = location_names.index(start_node)
        except ValueError:
            try:
                start_node = int(start_node)
            except ValueError:
                messagebox.showerror("Error", "Invalid Inputs.")
                return     
        
        try:        
            end_node = location_names.index(end_node)
        except ValueError:
            try:
                end_node = int(end_node)
            except ValueError:
                messagebox.showerror("Error", "Invalid Inputs.")
                return              
        return start_node, end_node
    
    
    def check_and_get_req(self):
        # Retrieve nodes to remove from the entry box
        global location_names
        if self.req_entry.get() is None:
            self.req_nodes = []
        else:
            temp = self.req_entry.get()
            try:
                temp = location_names.index(temp)
                self.req_nodes.append(temp)
                self.draw_graph([])  # Redraw the updated graph 
            except ValueError:
                try:
                    # Parse as a list of integers
                    temp = list(map(int, self.req_entry.get().split(",")))
                    for i in temp:
                        if i not in self.req_nodes:
                            self.req_nodes.append(i)
                    self.draw_graph([])  # Redraw the updated graph                    
                except ValueError:
                    messagebox.showerror("Error", "Invalid Inputs.")
                    return             
            

            
            
        
    #  Methods to draw the graph on canvas
    #===================================== 
    def draw_graph(self, path):            
        # Define positions for each node
        global positions
        pos = positions
        
        if(path):
            distance = self.calculate_total_distance(path)
            self.distance_label.config(text=f"Estimated distance: {distance:.2f}m")            
            
        # Create a matplotlib figure for the graph
        fig, ax = plt.subplots(figsize=(6, 8))
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
                
        background_image = mpimg.imread("map.jpg")  # Replace with your image file
        ax.imshow(background_image, extent=[0, 600, 0, 810]) #aspect='auto')
                
        canvas_agg = FigureCanvasTkAgg(fig, master=self.canvas)
        canvas_agg.get_tk_widget().pack()              
        
        # Draw edges (exclude edges with disabled nodes)
        active_edges = [(u, v) for u, v in G.edges 
                        if u not in self.disabled_nodes 
                        and v not in self.disabled_nodes
                        and (u, v) not in self.disabled_edges]
        nx.draw_networkx_edges(
            G, 
            pos, 
            ax=ax,
            edgelist=active_edges, 
            edge_color='#d2d2d4',    #d2d2d4
            alpha=0.5,
            width=0.7
        )
        
        # Draw disabled edges with a distinct color (optional)
        nx.draw_networkx_edges(
            G, 
            pos, 
            edgelist=list(self.disabled_edges), 
            ax=ax, 
            edge_color="lightgray", 
            style="dashed", 
            alpha=0.5,
            width=0.7
        )        
        
        # Draw all nodes
        node_colors = ['lightgray' if node in self.disabled_nodes
                       else 'lightblue' for node in G.nodes]
        nx.draw_networkx_nodes(
            G, 
            pos, 
            ax=ax, 
            nodelist=G.nodes, 
            node_color=node_colors, 
            alpha=0.5,
            node_size=5)        
             
            
        # Highlight the shortest path
        if path:
            path_node_colors = ['#58f5ed'] * len(path)
            path_node_colors[0] = 'red'
            path_node_colors[len(path)-1] = 'red'
          
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_nodes(
                G, 
                pos, 
                ax=ax, 
                nodelist=path, 
                node_color=path_node_colors, 
                alpha=0.7,
                node_size=6
            )
            nx.draw_networkx_edges(
                G, 
                pos, 
                ax=ax, 
                edgelist=path_edges, 
                edge_color='#58f5ed', 
                width=1
            )            

        # Hightlight the req_nodes
        nx.draw_networkx_nodes(
                G, 
                pos, 
                ax=ax, 
                nodelist=self.req_nodes, 
                node_shape='x',
                node_color='green', 
                node_size=7)       
     
        # Remove axes for a cleaner look
        ax.set_xlim(0, 600)
        ax.set_ylim(0, 800)
        ax.axis("off")
        
        # Track the last focused entry widget
        last_focused_entry = None
        last_click = None
    
        # Function to update last_focused_entry whenever an entry is focused
        def set_last_focused(event):
            nonlocal last_focused_entry
            last_focused_entry = event.widget        
            
        # Function to show node label on click
        def on_click(event):
            nonlocal last_click
            global location_names
            
            # Clear previous text box
            for txt in ax.texts:
                Artist.remove(txt)
            fig.canvas.draw_idle() 
            
            #double click to reset map
            if event.xdata>500:
                print("find...")
                self.req_nodes.clear()
                self.draw_graph([])  
                
            # Check if click is near a node and display its label
            for node, (x, y) in pos.items():
                if abs(event.xdata - x) < 5 and abs(event.ydata - y) < 5:
                    last_click = (event.xdata, event.ydata, node)
                    ax.text(
                            x, y, f"{location_names[node]}\n ID:{node}",
                            color="#535e7a", fontsize=5, ha="center", va="center",
                            bbox=dict(facecolor="lightblue", 
                                      edgecolor="lightblue", 
                                      boxstyle="round,pad=0.1")
                    )
                    fig.canvas.draw_idle()
                    
                    # Populate the last focused entry if it exists
                    if last_focused_entry:
                        last_focused_entry.delete(0, tk.END)
                        last_focused_entry.insert(0, f"{location_names[node]}")
                        last_focused_entry.focus()  # Refocus the entry to keep the cursor                    
                    
                    return  # Stop after finding the first matching node
            last_click = (event.xdata, event.ydata, None)


        # Toggle the active state of a node on double-click
        #===================================================
        def toggle_node(event):
            # getting the node
            nonlocal last_click
            x, y, last_click_node = last_click
        
            if last_click_node is not None:
                # Toggle the node's state: disable if active, enable if disabled
                if last_click_node in self.disabled_nodes:
                    self.disabled_nodes.discard(last_click_node)
                else:
                    self.disabled_nodes.add(last_click_node)
                    if last_click_node in self.req_nodes:
                        self.req_nodes.discard(last_click_node)
                self.draw_graph([])  # Redraw the updated graph
            else:
                toggle_edge(event, x, y)
                
                
        # Toggle the active state of a edge on double-click
        #===================================================               
        def toggle_edge(event, nx, ny):
            x, y, = nx, ny
            
            min_distance = float("inf")
            closest_edge = None
            
            # Find the closest edge to the click within a tolerance range
            for u, v in G.edges:
                ux, uy = pos[u]
                vx, vy = pos[v]
                
                # Calculate the perpendicular distance from the point to the line segment (u, v)
                edge_distance = abs((vy - uy) * x - (vx - ux) * y + vx * uy - vy * ux) / ((vy - uy)**2 + (vx - ux)**2) ** 0.5
                if edge_distance < min_distance and edge_distance < 10:  # Tolerance of 10 pixels
                    min_distance = edge_distance
                    closest_edge = (u, v)
          
                    
            if closest_edge is not None:
                # Toggle the edge's state: disable if active, enable if disabled
                if closest_edge in self.disabled_edges or (closest_edge[1], closest_edge[0]) in self.disabled_edges:
                    self.disabled_edges.discard(closest_edge)
                    self.disabled_edges.discard((closest_edge[1], closest_edge[0]))
                else:
                    self.disabled_edges.add(closest_edge)
                    
                # Redraw the updated graph  
                self.draw_graph([])            
        
    
    
    
        # Embed the matplotlib figure into the tkinter canvas
        canvas_agg.draw()    
        
        # Connect click event to on_click function
        fig.canvas.mpl_connect("button_press_event", on_click)          
        
        # Bind focus events to the entry widgets to track the last focused entry
        self.start_node_entry.bind("<FocusIn>", set_last_focused)
        self.end_node_entry.bind("<FocusIn>", set_last_focused)      
        self.req_entry.bind("<FocusIn>", set_last_focused)   
        
        # Embed the matplotlib figure into the tkinter canvas
        for widget in self.canvas.winfo_children():
            widget.destroy()
        canvas_agg = FigureCanvasTkAgg(fig, master=self.canvas)
        canvas_agg.draw()
        canvas_agg.get_tk_widget().pack(fill="both", expand=True)        
            
        # Bind double-click event to toggle node state
        canvas_agg.get_tk_widget().bind("<Double-Button-1>", toggle_node)           
        
            
            
            
            
            
            
            
            
            
    # Method to display the next/previous path in all_paths (DFS)
    #============================================================
    def show_next_path(self):
        if self.all_paths and self.index < len(self.all_paths) - 1:
            self.index += 1
            if self.index == 1:
                self.prev_button.config(state=tk.NORMAL)             
            elif self.index == len(self.all_paths) - 1:
                self.next_button.config(state=tk.DISABLED)  # Disable the "Next"
        self.draw_graph(self.all_paths[self.index]) 
            
    def show_prev_path(self):
        if self.all_paths and self.index > 0:
            self.index -= 1
            if self.index == len(self.all_paths) - 2:
                self.next_button.config(state=tk.NORMAL)             
            elif self.index == 0:
                self.prev_button.config(state=tk.DISABLED)  # Disable the "Prev"   
        self.draw_graph(self.all_paths[self.index])
    
    
    
    # Method to reset the graph to its original state
    #=================================================
    def reset_graph(self):
        # Clear disabled nodes and edges
        self.disabled_nodes.clear()
        self.disabled_edges.clear()
        self.req_nodes.clear()
        self.all_paths.clear()
        self.next_button.config(state=tk.DISABLED)
        self.prev_button.config(state=tk.DISABLED)
        
        # Redraw the original graph
        self.draw_graph([])
    
    
    # Method to get the total distance of a path
    #===========================================
    def calculate_total_distance(self, path):
        total_distance = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            if G.has_edge(u, v):
                total_distance += G[u][v]['weight']
        return total_distance
    
    
    # Method to get the subgraph (active nodes and edges)
    #====================================================
    def get_active_subgraph(self):
        # Filter out nodes and edges associated with disabled nodes
        active_nodes = [node for node in G.nodes if node not in self.disabled_nodes]
        active_edges = [(u, v, G[u][v]) for u, v in G.edges 
                        if u in active_nodes and v in active_nodes 
                        and (u,v) not in self.disabled_edges]
    
        # Create a subgraph with only the active nodes and edges
        active_subgraph = nx.Graph()
        active_subgraph.add_nodes_from(active_nodes)
        active_subgraph.add_edges_from(active_edges)
    
        return active_subgraph
        
        
    # Methods to start BFS
    #======================
    def bfs(self):
        start, end = self.check_input()
        active_subgraph = self.get_active_subgraph()
        
        #disable unrealted widgets
        self.req_nodes.clear()
        self.next_button.config(state=tk.DISABLED)
        self.prev_button.config(state=tk.DISABLED)
        
        # Find the shortest path using BFS
        if start in self.disabled_nodes or end is self. disabled_nodes:
            messagebox.showerror("Error", "No path found.")
            
        path = bfs_shortest_path(active_subgraph, start, end)

        # Draw the path on the canvas
        if path:
            self.draw_graph(path)
        else:
            messagebox.showerror("Error", "No path found.")
        
    
    # Methods to start DFS
    #======================        
    def dfs(self):
        start, end = self.check_input()  
        active_subgraph = self.get_active_subgraph()
        
        #Find paths that pass through required nodes using DFS
        if start in self.disabled_nodes or end is self. disabled_nodes:
            messagebox.showerror("Error", "No path found.")        
        
        max_depth=5
        self.all_paths.clear()
        while max_depth<15:
            self.all_paths += dfs_all_paths(active_subgraph, start, end, self.req_nodes, max_depth)
            if len(self.all_paths)>5:
                self.all_paths = self.all_paths[:5]
                break
            else:
                max_depth+=1
            
        #self.all_paths = dfs_all_paths(active_subgraph, start, end, self.req_nodes)
        self.index = 0
    
        # Enable the "Next" button if paths are found
        if self.all_paths:
            self.next_button.config(state=tk.NORMAL)
            self.draw_graph(self.all_paths[self.index])
        else:
            self.next_button.config(state=tk.DISABLED)
            messagebox.showerror("Error", "No path found.")
            
            
    # Methods to start Dijkstra's algo
    #==================================
    def dijkstra(self):
        start, end = self.check_input()  
        active_subgraph = self.get_active_subgraph()
        
        #disable unrealted widgets
        self.req_nodes.clear()
        self.next_button.config(state=tk.DISABLED)
        self.prev_button.config(state=tk.DISABLED)        
        
        # Find the shortest path using Dijkstra's
        if start in self.disabled_nodes or end is self. disabled_nodes:
            messagebox.showerror("Error", "No path found.")        
        
        path, total_weight = dijkstra_shortest_path(active_subgraph, start, end)
        
        # Draw the path on the canvas
        if path:
            self.draw_graph(path)  
        else:
            messagebox.showerror("Error", "No path found.")
            
            
root = tk.Tk()

# Create a networkx graph
G = nx.Graph()
G.add_weighted_edges_from(edges) 

app = GUI(root)
root.mainloop()