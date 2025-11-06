from pathlib import Path



def generate_readme_profile(theme, **kwargs):
    """ Generate GitHub profile README based on the selected theme and user info."""
    # Readme theme profile
    with open(f"src/themes/{theme}/profile.txt") as f:
        profile = f.read()
        
    # Get all possible placeholders from the profile
    import re
    placeholders = re.findall(r'\{ (\w+) \}', profile)
        
    # Replace placeholders with items 
    for placeholder in placeholders:
        for item, value in kwargs.items():
            if placeholder in kwargs:
                # Skip empty values
                if not value or (isinstance(value, str) and value.strip() == ""):
                    profile = profile.replace(f"{{ {item} }}", '')
                    continue

                # Skip items that doesn't exist on theme
                item_path = Path(f"src/themes/{theme}/{item}.txt")
                if not item_path.exists():
                    continue
                                
                print(f"{item}: {value}")
                # Replace placeholders with item
                with open(item_path) as f:
                    profile_item = f.read()
                profile_item = profile_item.replace("{ value }", value)
                profile = profile.replace(f"{{ {item} }}", profile_item)
            
            else:
                # Remove placeholder if not in kwargs
                profile = profile.replace(f"{{ {placeholder} }}", '')

    return profile



if __name__ == "__main__":
    kwarg = {}
    kwarg['name'] = "John Doe"
    kwarg['degree'] = "Bachelor of Science in Computer Science"
    
    theme = "default"
    readme_content = generate_readme_profile(theme, **kwarg)    
