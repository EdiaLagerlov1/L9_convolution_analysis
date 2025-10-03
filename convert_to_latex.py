import subprocess
import matplotlib.pyplot as plt

print("Running convolution_analysis.py...")

# Read and execute the original script
with open('convolution_analysis.py', 'r') as f:
    code = f.read()

# Replace plt.show() to prevent showing before saving
code = code.replace('plt.show()', '# plt.show()')

# Execute the modified code
exec(code)

# Now save the figure that was just created
fig = plt.gcf()  # Get current figure
fig.savefig('convolution_analysis.pdf', bbox_inches='tight', dpi=300)
print("✓ Saved graphs to convolution_analysis.pdf")

# Create simple LaTeX document
latex_content = r"""\documentclass{article}
\usepackage{graphicx}
\usepackage{geometry}
\geometry{margin=1in}

\title{Convolution Analysis}
\author{}
\date{\today}

\begin{document}
\maketitle

\begin{figure}[h]
    \centering
    \includegraphics[width=\textwidth]{convolution_analysis.pdf}
    \caption{Convolution Analysis Results}
\end{figure}

\end{document}
"""

# Save LaTeX file
with open('convolution_analysis_report.tex', 'w') as f:
    f.write(latex_content)
print("✓ Created convolution_analysis_report.tex")

# Compile to PDF
try:
    result = subprocess.run(['pdflatex', '-interaction=nonstopmode',
                             '-jobname=convolution_analysis_report',
                             'convolution_analysis_report.tex'],
                            capture_output=True, text=True)
    if result.returncode == 0:
        print("✓ Created convolution_analysis_report.pdf")
    else:
        print("✗ Error compiling LaTeX:")
        print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)

    # Clean up auxiliary files
    import os

    for ext in ['.aux', '.log']:
        try:
            os.remove(f'convolution_analysis_report{ext}')
        except:
            pass
except FileNotFoundError:
    print("✗ Error: pdflatex not found. Please install LaTeX.")
    print("  The convolution_analysis.pdf and convolution_analysis_report.tex files are ready.")

# Show the graphs
plt.show()