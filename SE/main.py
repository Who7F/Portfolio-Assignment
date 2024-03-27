import tkinter as tk
import mathsSim


def permtation_word_input(in_text, out_text):
    anc: int = mathsSim.permtation_word(in_text.get("1.0", "end-1c"))
    out_text.insert('1.0', anc)
    

def permtation_word(frame):
    header = tk.Label(frame, text = "Permtation on letters  in words", bg = '#7D9DD3', fg = '#FFF', font = ("TkMenuFont", 14))
    in_text = tk.Text(frame, height = 1, width = 20)
    out_text = tk.Text(frame, height = 1, width = 8)
    button = tk.Button(frame, text = "Clickly", font = ("TkMenuFont", 14), command = lambda:permtation_word_input(in_text, out_text))

    header.pack(pady=5)
    in_text.pack(pady=5)
    button.pack(pady=5)
    out_text.pack(pady=5)
    

def permtation_num_input(in_text_n, in_text_r, out_text):
    try:
        anc: int = mathsSim.permtation_num(int(in_text_n.get("1.0", "end-1c")), int(in_text_r.get("1.0", "end-1c")))
        out_text.insert('1.0', anc)
    except:
        print('permtation_num_input Need to be int')
        out_text.insert('1.0', "err")
        

def permtation_num(frame):
    header = tk.Label(frame, text = "Permtation on numbers", bg = '#7D9DD3', fg = '#FFF', font = ("TkMenuFont", 14))
    in_text_n = tk.Text(frame, height = 1, width = 5)
    in_text_r = tk.Text(frame, height = 1, width = 5)
    out_text = tk.Text(frame, height = 1, width = 8)
    button = tk.Button(frame, text = "Clickly", font = ("TkMenuFont", 14), command = lambda:permtation_num_input(in_text_n, in_text_r, out_text))

    frame_text = tk.Frame(frame, width=50, bg="#7D9DD3", height=20)
    in_text_n = tk.Text(frame_text, height = 1, width = 5)
    division = tk.Label(frame_text, text = " / ", bg = '#7D9DD3', fg = '#FFF', font = ("TkMenuFont", 14))
    in_text_r = tk.Text(frame_text, height = 1, width = 5)
    
    header.pack(pady=5)
    frame_text.pack()
    in_text_n.pack(pady=5, side ='left')
    division.pack(pady=5, side ='left')
    in_text_r.pack(pady=5, side ='left')
    button.pack(pady=5)
    out_text.pack(pady=5)
    

def add_list(in_text_a, in_text_b, my_list, out_text):
    try:
        my_list.append([int(in_text_a.get("1.0", "end-1c")), int(in_text_b.get("1.0", "end-1c"))])
        text = in_text_a.get("1.0", "end-1c")+'/'+in_text_b.get("1.0", "end-1c")+','
        
        out_text.insert('1.0', text)
        print(my_list)
    except:
        print('prob Need to be int')
        

def probability_input(actions, my_list, out_text):
    anc = 0
    match actions:
        case 'and':
            anc = mathsSim.chance_on_and(my_list)
        case 'or':
            anc = mathsSim.chance_on_or(True, my_list)
        case 'or_other':
            anc = mathsSim.chance_on_or(False, my_list)
        case _:
            print('No case')
            anc = 'err'
    print(anc)
    out_text.insert('1.0', anc)

        
def probability(frame):
    my_list = []
    header = tk.Label(frame, text = "Probability", bg = '#7D9DD3', fg = '#FFF', font = ("TkMenuFont", 14))

    frame_text = tk.Frame(frame, width=50, bg="#7D9DD3", height=20)
    in_text_a = tk.Text(frame_text, height = 1, width = 5)
    out_of = tk.Label(frame_text, text = " out of ", bg = '#7D9DD3', fg = '#FFF', font = ("TkMenuFont", 14))
    in_text_b = tk.Text(frame_text, height = 1, width = 5)
    hold_text = tk.Text(frame, height = 1, width = 12)
    out_text = tk.Text(frame, height = 1, width = 8)
    add_button = tk.Button(frame, text = "Add", font = ("TkMenuFont", 14), command = lambda:add_list(in_text_a, in_text_b, my_list, hold_text))

    frame_button = tk.Frame(frame, width=50, bg="#7D9DD3", height=20)
    button_and = tk.Button(frame_button, text = "And", font = ("TkMenuFont", 14), command = lambda:probability_input('and', my_list, out_text))
    button_or = tk.Button(frame_button, text = "Or", font = ("TkMenuFont", 14), command = lambda:probability_input('or', my_list, out_text))
    button_or_other = tk.Button(frame_button, text = "Or other", font = ("TkMenuFont", 14), command = lambda:probability_input('or_other', my_list, out_text))

    header.pack(pady=5)

    frame_text.pack()
    in_text_a.pack(pady=5, side ='left')
    out_of.pack(pady=5, side ='left')
    in_text_b.pack(pady=5, side ='left')
    
    add_button.pack(pady=5)
    hold_text.pack(pady=5)
    
    frame_button.pack()
    button_and.pack(pady=5, side ='left')
    button_or.pack(pady=5, side ='left')
    button_or_other.pack(pady=5, side ='left')
    
    out_text.pack(pady=5)

    
def add_num(in_text_a, my_list, out_text):
    try:
        my_list.append(int(in_text_a.get("1.0", "end-1c")))
        text = in_text_a.get("1.0", "end-1c")+','
        
        out_text.insert('1.0', text)
    except:
        print('av Need to be int')
        

def average_input(actions, my_list, out_text):
    anc = mathsSim.avage(actions, my_list)
    out_text.insert('1.0', anc)

        
def average(frame):
    my_list = []
    header = tk.Label(frame, text = "Average", bg = '#7D9DD3', fg = '#FFF', font = ("TkMenuFont", 14))
    
    in_text = tk.Text(frame, height = 1, width = 5)
    hold_text = tk.Text(frame, height = 1, width = 12)
    out_text = tk.Text(frame, height = 1, width = 8)
    add_button = tk.Button(frame, text = "Add", font = ("TkMenuFont", 14), command = lambda:add_num(in_text, my_list, hold_text))

    frame_button = tk.Frame(frame, width=50, bg="#7D9DD3", height=20)
    button_mean = tk.Button(frame_button, text = "Mean", font = ("TkMenuFont", 14), command = lambda:probability_input('mean', my_list, out_text))
    button_mode = tk.Button(frame_button, text = "Mode", font = ("TkMenuFont", 14), command = lambda:probability_input('mode', my_list, out_text))
    button_medum = tk.Button(frame_button, text = "Medum", font = ("TkMenuFont", 14), command = lambda:probability_input('medum', my_list, out_text))

    header.pack(pady=5)
    in_text.pack(pady=5)

    add_button.pack(pady=5)
    hold_text.pack(pady=5)

    frame_button.pack()
    button_medum.pack(pady=5, side ='left')
    button_mode.pack(pady=5, side ='left')    
    button_mean.pack(pady=5, side ='left')
    
    out_text.pack(pady=5)
    
    
def main():
    root = tk.Tk()
    root.title('W3CPS')
    root.eval("tk::PlaceWindow . center")
    THE_WIDTH = 500

    frame = tk.Frame(root, width=THE_WIDTH, height=500, bg = "#7D9DD3")
    frame.grid(row = 0, column = 0)
    frame.pack_propagate(False)

    frame_top = tk.Frame(frame, height=200, bg = "#7D9DD3")
    frame_bottom = tk.Frame(frame, bg = "#7D9DD3" ,height=328)
    # frame_sub.pack(pady=20,padx=20)
    frame_top.pack(fill = 'x', side ='top')
    frame_bottom.pack(fill = 'x', side ='top')

    frame_top_left = tk.Frame(frame_top, width=400, bg = "#7D9DD3", height=190)
    frame_top_right = tk.Frame(frame_top, width=400, bg = "#7D9DD3", height=190)

    frame_top_left.pack(pady=2,padx=5, side ='left')
    frame_top_right.pack(pady=2,padx=5 , side ='left')


    permtation_word(frame_top_left)
    permtation_num(frame_top_right)

    frame_bottom_left = tk.Frame(frame_bottom, width=400, bg = "#7D9DD3", height=190)
    frame_bottom_right = tk.Frame(frame_bottom, width=400, bg = "#7D9DD3", height=190)

    frame_bottom_left.pack(pady=2,padx=5, side ='left')
    frame_bottom_right.pack(pady=2,padx=5 , side ='left')
    
    probability(frame_bottom_left)
    average(frame_bottom_right)
    
    root.mainloop()

if __name__=='__main__':
    main()
