document.addEventListener("DOMContentLoaded", () => {
    const terminalOutput = document.getElementById("terminal-output");
    const cursor = document.createElement("span");
    cursor.className = "cursor";
    cursor.textContent = "|";
    terminalOutput.appendChild(cursor);
    
    const commands = [
        "Initializing OSINT framework...",
        "Gathering data from sources...",
        "Analyzing information...",
        "Generating report...",
        "Completed! All systems operational."
    ];

    let commandIndex = 0;

    function typeCommand() {
        if (commandIndex < commands.length) {
            terminalOutput.innerHTML += `<div>${commands[commandIndex]}</div>`;
            commandIndex++;
            setTimeout(typeCommand, 2000);
        } else {
            cursor.style.display = "none"; // Hide cursor after completion
        }
    }

    function toggleCursor() {
        cursor.style.visibility = (cursor.style.visibility === 'hidden') ? 'visible' : 'hidden';
    }
    
    setInterval(toggleCursor, 500); // Blinking cursor
    typeCommand(); // Start typing commands

    // Interactive button to refresh data
    const refreshButton = document.getElementById("refresh-data");
    refreshButton.addEventListener("click", () => {
        terminalOutput.innerHTML = ""; // Clear previous output
        commandIndex = 0; // Reset command index
        typeCommand(); // Re-run command simulation
    });
});
```

Make sure to include a corresponding HTML structure with an element having `id="terminal-output"` and a button with `id="refresh-data"` for the script to function correctly.