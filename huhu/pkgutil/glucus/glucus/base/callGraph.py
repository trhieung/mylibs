import subprocess
from pathlib import Path

class callGraph:
    @staticmethod
    def run(file_paths: list[str], dot_file="callgraph.dot", png_file="callgraph.png"):
        # Ensure all paths exist
        for file in file_paths:
            if not Path(file).exists():
                raise FileNotFoundError(f"File not found: {file}")
        
        try:
            # Step 1: Generate the .dot file using pyan3
            subprocess.run(
                ["pyan3", *file_paths, "--dot", "--uses", "--no-defines"],
                check=True,
                stdout=open(dot_file, "w")
            )

            # Step 2: Generate the .png file using dot
            subprocess.run(
                ["dot", "-Tpng", dot_file, "-o", png_file],
                check=True
            )

            print(f"[+] Call graph saved as: {png_file}")

        except subprocess.CalledProcessError as e:
            print("[-] Error during subprocess:", e)
        except Exception as e:
            print("[-] General error:", e)