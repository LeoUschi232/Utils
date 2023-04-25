from subjects import Subject

subject = Subject.QM
sheet = 2
scale = 0.45
number_of_empty_lines = 10
exercises = [
    "1a", "1b", "1c", "1d", "1e", "1f", "2a", "2b", "2c"
]

with open("current_sheet_template.txt", "w") as file:
    header = (
        "\\documentclass[10pt,a4paper]{scrartcl}\n"
        "\n"
        "\\usepackage{amsfonts}\n"
        "\\usepackage{amsmath}\n"
        "\\usepackage{amssymb}\n"
        "\\usepackage{array}\n"
        "\\usepackage{blindtext}\n"
        "\\usepackage{braket}\n"
        "\\usepackage{caption}\n"
        "\\usepackage{chemfig}\n"
        "\\usepackage{csquotes}\n"
        "\\usepackage{enumitem}\n"
        "\\usepackage{esint}\n"
        "\\usepackage{float}\n"
        "\\usepackage{graphicx}\n"
        "\\usepackage{listings}\n"
        "\\usepackage{mathtools}\n"
        "\\usepackage{parskip}\n"
        "\\usepackage{relsize}\n"
        "\\usepackage{setspace}\n"
        "\\usepackage{subcaption}\n"
        "\\usepackage{todonotes}\n"
        "\\usepackage{url}\n"
        "\\usepackage{xcolor}\n"
        "\\usepackage{xfp}\n"
        "\n"
        "\\usepackage[english]{babel}\n"
        "\\usepackage[T1]{fontenc}\n"
        "\\usepackage[colorlinks, linkcolor=black, citecolor=black, urlcolor=black]{hyperref}\n"
        "\\usepackage[utf8]{inputenc}\n"
        "\\usepackage[left=2cm, right=2cm, top=2cm, bottom=2.3cm]{geometry}\n"
        "\\usepackage[document]{ragged2e}\n"
        "\n"
        "\\onehalfspacing\n"
        "\\setlength{\\parindent}{0em}\n"
        "\n"
        "\\captionsetup[table]{position=above, skip=0cm}\n"
        "\\captionsetup[figure]{position=below, skip=5cm}\n"
        "\\captionsetup[figure]{position=above, skip=0cm}\n"
        "\n"
        "\\DeclareMathOperator{\\tacticalAnd}{\\qquad\\wedge\\qquad}\n"
        "\\DeclareMathOperator{\\ontop}{\\mathrel{\\stackrel}}\n"
        "\\DeclareMathOperator{\\equivalent}{\\qquad\\Longleftrightarrow\\qquad}\n"
        "\\DeclareMathOperator{\\means}{\\qquad\\Longrightarrow\\qquad}\n"
        "\\DeclareMathOperator{\\real}{\mathbb{R}}\n"
        "\\DeclareMathOperator{\\natur}{\mathbb{N}}\n"
        "\\DeclareMathOperator{\\E}{\\mathcal{E}}\n"
        "\n"
        "\n\lstset{\n"
        "    language=Python,\n"
        "    basicstyle=\\ttfamily\small,\n"
        "    keywordstyle=\color{blue},\n"
        "    stringstyle=\color{red},\n"
        "    commentstyle=\color{green!70!black},\n"
        "    numbers=left,\n"
        "    numberstyle=\\tiny\color{gray},\n"
        "    frame=single,\n"
        "    showstringspaces=false,\n"
        "    tabsize=4,\n"
        "    captionpos=b,\n"
        "    breaklines=true,\n"
        "    breakatwhitespace=true,\n"
        "    escapeinside={(*@}{@*)}\n"
        "}\n"
        "\n"        
        "\\title{\\textbf{"
        f"{subject.long_name}"
        "} \\\\ \\vspace{5pt} \\large TUM "
        f"{subject.field} \\\\ {subject.name} Sheet {sheet}"
        "}\n"
        "\\author{Leonard Uscinowicz}\n"
        "\n"
        "\\begin{document}\n"
        "\n"
        "\\justifying\n"
        "\\maketitle\n\n"
    )
    file.write(header)

    for exercise in exercises:
        current_figure_enumeration = (
                "\\begin{figure}[H]\n" +
                f"    \centering\n" +
                f"    \includegraphics[scale={scale}]" + "{" + f"{subject.name}Sheet{sheet}Exc{exercise}" + "}\n" +
                f"    \caption" + "{" + f"{subject.name}Sheet{sheet}Exc{exercise}" + "}\n" +
                f"    \label" + "{fig:" + f"{subject.name}Sheet{sheet}Exc{exercise}" + "}\n" +
                f"\end" + "{figure}\n" +
                (number_of_empty_lines * "\n")
        )
        file.write(current_figure_enumeration)

    ending = "\\end{document}"
    file.write(ending)
