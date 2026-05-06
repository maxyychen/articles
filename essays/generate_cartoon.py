import matplotlib.pyplot as plt

with plt.xkcd():
    # Smaller figure size
    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.axis('off')
    
    # Closer positions, removed Scalability from Requirements
    boxes = [
        {"text": "1. Requirements\n(The 'What')", "pos": (0.15, 0.7), "color": "lightpink"},
        {"text": "2. Architecture\nas Code", "pos": (0.5, 0.7), "color": "skyblue"},
        {"text": "3. Code", "pos": (0.85, 0.7), "color": "lightgreen"}
    ]
    
    for box in boxes:
        ax.text(box["pos"][0], box["pos"][1], box["text"], 
                ha='center', va='center', size=11,
                bbox=dict(boxstyle='round,pad=0.5', fc=box["color"], ec='black', lw=1.5))
    
    # Tools sub-box
    tools_text = "Tools: PlantUML, Mermaid, C4 DSL\n(Text-based, Versioned, Reviewable)"
    ax.text(0.5, 0.45, tools_text, 
            ha='center', va='center', size=10, color='darkblue',
            bbox=dict(boxstyle='sawtooth,pad=0.5', fc='white', ec='skyblue', lw=1))
    
    # Shorter arrows
    ax.annotate('', xy=(0.38, 0.7), xytext=(0.28, 0.7),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    ax.annotate('', xy=(0.72, 0.7), xytext=(0.62, 0.7),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    ax.set_title("The AI Architecture Pipeline", size=14, pad=10)
    
    plt.tight_layout()
    plt.savefig('ai_architecture_cartoon.png', dpi=150, bbox_inches='tight')
