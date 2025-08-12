import re

class Cake_World:
    def __init__(self, filename="cake.txt"):
        self.filename = filename

    def add_new_recipe(self):
        cake_name = input("Enter the cake name: ").strip()
        cake_ingredients = input("Enter the cake ingredients: ").strip()
        cake_recipe = input("Enter the cake recipe: ").strip()

        try:
            with open(self.filename, "a", encoding="utf-8") as f:
                f.write(f"Title:{cake_name}\n")
                f.write(f"Ingredients:{cake_ingredients}\n")
                f.write(f"Recipe:{cake_recipe}\n")
                f.write("==========================\n")
            print("✅ Recipe added successfully.")
        except Exception as e:
            print(f"❌ Error saving recipe: {e}")

    def search_recipe(self, field):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("⚠️ No file found")
            return

        value = input(f"Enter the {field.lower()} to search: ").strip()
        pattern = rf"^{re.escape(field)}:\s*{re.escape(value)}$"
        found = False
        block = []

        for line in lines:
            if line.strip() == "==========================":
                if any(re.match(pattern, l.strip(), re.IGNORECASE) for l in block):
                    print("\n".join(block))
                    print("==========================")
                    found = True
                block = []
            else:
                block.append(line.strip())

        # Last block check (if file doesn't end with ==========================)
        if block:
            if any(re.match(pattern, l.strip(), re.IGNORECASE) for l in block):
                print("\n".join(block))
                print("==========================")
                found = True

        if not found:
            print(f"❌ No recipe found with that {field.lower()}.")

    def delete_recipe(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("⚠️ No file found")
            return

        value = input("Enter cake name (Title) to delete: ").strip()
        pattern = rf"^Title:\s*{re.escape(value)}"
        new_lines, block = [], []
        found_any = False

        for line in lines:
            if line.strip() == "==========================":
                if any(re.search(pattern, l, re.IGNORECASE) for l in block):
                    print("\n🔍 Matched Recipe:")
                    print("".join(block))
                    confirm = input("Do you want to delete this recipe? (yes/no): ").strip().lower()
                    if confirm == "yes":
                        found_any = True  # skip writing
                    else:
                        new_lines.extend(block + ["==========================\n"])
                else:
                    new_lines.extend(block + ["==========================\n"])
                block = []
            else:
                block.append(line)

        if found_any:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print("✅ Selected recipe deleted.")
        else:
            print("❌ No recipe found with that title.")

    def update_recipe(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("⚠️ No file found")
            return

        value = input("Enter cake name (Title) to update: ").strip()
        pattern = rf"^Title:\s*{re.escape(value)}"
        new_lines, block = [], []
        found_any = False

        for line in lines:
            if line.strip() == "==========================":
                if any(re.search(pattern, l, re.IGNORECASE) for l in block):
                    print("\n🔍 Matched Recipe:")
                    print("".join(block))
                    confirm = input("Do you want to update this recipe? (yes/no): ").strip().lower()
                    if confirm == "yes":
                        found_any = True
                        new_cake_name = input("Enter new cake name: ").strip()
                        new_ingredients = input("Enter new ingredients: ").strip()
                        new_recipe = input("Enter new recipe: ").strip()

                        new_lines.append(f"Title:{new_cake_name}\n")
                        new_lines.append(f"Ingredients:{new_ingredients}\n")
                        new_lines.append(f"Recipe:{new_recipe}\n")
                        new_lines.append("==========================\n")
                    else:
                        new_lines.extend(block + ["==========================\n"])
                else:
                    new_lines.extend(block + ["==========================\n"])
                block = []
            else:
                block.append(line)

        if found_any:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print("✅ Recipe updated successfully.")
        else:
            print("❌ No matching recipe found.")

    def list_cake_names(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("⚠️ No file found")
            return

        titles = [line.strip().replace("Title:", "") for line in lines if line.startswith("Title:")]
        if titles:
            print("📋 All Cake Names:")
            for idx, title in enumerate(titles, 1):
                print(f"{idx}. {title}")
        else:
            print("No cake names found.")

    def print_all_recipes(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("⚠️ No file found")
            return

        block = []
        recipe_num = 1
        found = False

        for line in lines:
            if line.strip() == "==========================":
                if block:
                    print(f"\nRecipe {recipe_num}:")
                    print("".join(block).strip())
                    recipe_num += 1
                    found = True
                block = []
            else:
                block.append(line)

        if not found:
            print("❌ No recipe found.")


print("______ Welcome To The Cake World ______\n")

if __name__ == "__main__":
    obj = Cake_World()
    while True:
        print("\n===== Cake World Menu =====")
        print("1. Add Recipe")
        print("2. Search Recipe")
        print("3. Delete Recipe")
        print("4. Update Recipe")
        print("5. List All Cake Names")
        print("6. Print All Recipes")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            obj.add_new_recipe()
        elif choice == "2":
            print("\nSearch by (Title / Ingredients / Recipe)")
            field = input("Enter field name: ").strip().capitalize()
            obj.search_recipe(field)
        elif choice == "3":
            obj.delete_recipe()
        elif choice == "4":
            obj.update_recipe()
        elif choice == "5":
            obj.list_cake_names()
        elif choice == "6":
            obj.print_all_recipes()
        elif choice == "7":
            print("👋 Exiting Cake World. Goodbye!")
            break
        else:
            print("❌ Invalid input. Try again.")
