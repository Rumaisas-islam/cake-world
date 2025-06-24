import re
class Cake_World:
  def __init__(self,filename="cake.txt"):
    self.filename=filename
  def add_new_recipe(self):
    cake_name=input("Enter the cake name: ")
    cake_ingredients=input("Enter the cake ingredients: ")
    cake_recipe=input("Enter the cake recipe: ")
    try:
      with open(self.filename,"a") as f:
        f.write("======================================\n")
        f.write(f"Cake_Name:{cake_name}\n")
        f.write(f"Cake_Ingredients:{cake_ingredients}\n")
        f.write(f"Cake_Recipe:{cake_recipe}\n")
        f.write("======================================\n")
      print("Recipe added successfully.")
    except Exception as e:
      print(f"Error saving recipe:{e}")
      return
  def view_recipe(self):
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("No file found with that name")
      return
    cake_name=input("Enter the cake name: ")
    pattern = rf"^Cake_Name:{re.escape(cake_name)}\b.*"
    found=False
    for i,line in enumerate(lines):
      if re.match(pattern,line,re.IGNORECASE):
        for j in range(i-1,i+4):
          if 0<=j<len(lines):
            print(lines[j].strip())
        found=True
        break
    if not found:
      print("No recipe found with that cake_name")
  def delete_recipe(self):
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("No file found of that name")
      return
    cake_name=input("Enter the cake name: ")
    pattern = rf"^Cake_Name:{re.escape(cake_name)}\b.*"
    new_lines=[]
    found=False 
    i=0
    while i<len(lines):
      line=lines[i]
      if re.match(pattern,line,re.IGNORECASE):
        found=True 
        while i>0 and not lines[i-1].startswith("="):
          i-=1 
        while i<len(lines) and not lines[i].startswith("="):
          i+=1 
        if i<len(lines):
          i+=1
      else:
        new_lines.append(line)
        i+=1 
    if found:
      with open(self.filename,"w") as f:
        f.write("".join(new_lines))
      print("Recipe deleted successfully!")

    else:
      print("No recipe found of this name")
  def edit_recipe(self):
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("No file found of this name")
      return
    cake_name=input("Enter the cake_name: ")
    pattern = rf"^Cake_Name:{re.escape(cake_name)}\b.*"
    new_lines=[]
    found=False 
    i=0 
    while i<len(lines):
      line=lines[i]
      if re.match(pattern,line,re.IGNORECASE):
        found=True 
        while i>0 and not lines[i-1].startswith("="):
          i-=1 
        while i<len(lines) and not lines[i].startswith("="):
          i+=1
        if i<len(lines):
          i+=1
        
        new_cake_name=input("Enter the cake name: ")
        new_cake_ingredients=input("Enter the ingredients: ")
        new_cake_recipe=input("Enter the recipe: ")

        new_lines.append("======================================\n")
        new_lines.append(f"Cake_Name:{new_cake_name}\n")
        new_lines.append(f"Cake_Ingredients:{new_cake_ingredients}\n")
        new_lines.append(f"Cake_Recipe:{new_cake_recipe}\n")
        new_lines.append("======================================\n")

      else:
        new_lines.append(line)
        i+=1 
    if found:
      with open(self.filename,"w") as f:
        f.write("".join(new_lines))
      print("Recipe updated successfully!")
    else:
      print("No recipe found of this name")
  def list_all_cake_names(self):
    try:
        with open(self.filename,"r") as f:
            lines=f.readlines()
        names=[line.strip().replace("Cake_Name:","") for line in lines if line.startswith("Cake_Name:")]
        if names:
            print("\n-----Saved Cake Names-----")
            for idx,name in enumerate(names,1):
                print(f"{idx}.{name}")
            print("======================================\n")
        else:
            print("No cake name found")
    except FileNotFoundError:
        print("No cake file found")
  def print_all_recipes(self):
    try:
      with open(self.filename,"r") as f:
        content=f.read().strip()
        print("\n----- All Saved Recipes -----\n")
        parts = re.split(r"(=+\n)", content)
        recipe_block=""
        recipe_count=1 
        for part in parts:
          recipe_block+=part 
          if re.fullmatch(r"=+\n", part):
            print(f"Recipe {recipe_count}")
            print(recipe_block)
            print()
            recipe_block=""
            recipe_count+=1 
    except FileNotFoundError:
      print("No file found")
print("______WElcome To The Cake World______\n")
obj=Cake_World()
while True:
  menu=input("What you want to do\n1.Add New Recipe\n2.View Recipe by Cake Name\n3.Delete Recipe by Cake Name\n4.Edit Recipe\n5.List All Cake Names\n6.Print All Recipes\n(1/2/3/4/5/6) or 'q'to quit: ")
  if menu == "1":
    obj.add_new_recipe()
  elif menu == "2":
    obj.view_recipe()
  elif menu == "3":
    obj.delete_recipe()
  elif menu == "4":
    obj.edit_recipe()
  elif menu == "5":
    obj.list_all_cake_names()
  elif menu == "6":
    obj.print_all_recipes()
  elif menu.lower() == "q":
    break
    
