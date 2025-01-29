document.getElementById('searchInput').addEventListener('input', function(e) {
    const searchText = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('tbody tr');
    
    rows.forEach(row => {
        const nameCell = row.cells[0].textContent.toLowerCase();  // Name
        const phoneCell = row.cells[1].textContent.toLowerCase();  // Phone
        const emailCell = row.cells[2].textContent.toLowerCase();  // Email
        const typeCell = row.cells[3].textContent.toLowerCase();   // Type
        //const text = row.textContent.toLowerCase();
        // If any cell in the row matches the search text, show the row, otherwise hide it
        if (nameCell.includes(searchText) || 
            phoneCell.includes(searchText) || 
            emailCell.includes(searchText) || 
            typeCell.includes(searchText)) {
            row.style.display = ''; // Show row
        } else {
            row.style.display = 'none'; // Hide row
        }
    });
});