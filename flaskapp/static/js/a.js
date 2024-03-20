// function sortTable(columnIndex) {
//     var table, rows, switching, i, x, y, shouldSwitch;
//     table = document.getElementById("commentTable");
//     switching = true;
//     while (switching) {
//         switching = false;
//         rows = table.rows;
//         for (i = 1; i < (rows.length - 1); i++) {
//             shouldSwitch = false;
//             x = rows[i].getElementsByTagName("td")[columnIndex];
//             y = rows[i + 1].getElementsByTagName("td")[columnIndex];
//             if (parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
//                 shouldSwitch = true;
//                 break;
//             }
//         }
//         if (shouldSwitch) {
//             rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
//             switching = true;
//         }
//     }
// }

function sortTable(columnIndex) {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("commentTable");
    console.log("tableeee---", table)
    switching = true;
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;

            // Satır içindeki sütun sayısı kontrolü
            if (columnIndex < rows[i].cells.length && columnIndex < rows[i + 1].cells.length) {
                x = rows[i].getElementsByTagName("td")[columnIndex];
                y = rows[i + 1].getElementsByTagName("td")[columnIndex];

                // null ya da undefined kontrolü
                if (x && y && x.innerHTML && y.innerHTML && parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}