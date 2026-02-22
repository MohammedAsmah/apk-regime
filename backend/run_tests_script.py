import subprocess
import sys
import os

def run_tests(app_name, output_file):
    print(f"Running tests for {app_name}...")
    base_dir = r"C:\Users\DELL\Desktop\APK-Regimes-Perte-de-Poids\backend"
    with open(os.path.join(base_dir, output_file), 'w', encoding='utf-8') as f:
        process = subprocess.Popen(
            [sys.executable, 'manage.py', 'test', app_name],
            stdout=f,
            stderr=subprocess.STDOUT,
            cwd=base_dir
        )
        process.wait()
    print(f"Finished {app_name}. Results in {output_file}")

if __name__ == "__main__":
    run_tests('users', 'users_final_results.txt')
    run_tests('nutrition', 'nutrition_final_results.txt')
