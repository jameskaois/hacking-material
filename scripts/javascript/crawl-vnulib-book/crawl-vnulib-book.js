let s = document.createElement("script");
s.src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js";
s.onload = () => {
    console.log("html2canvas loaded ✅");

    let s2 = document.createElement("script");
    s2.src = "https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js";
    s2.onload = () => {
        console.log("✅ jsPDF loaded")
        const { jsPDF } = window.jspdf;
        const pdf = new jsPDF("p", "pt", "a4");

        let pages = document.querySelectorAll('.page[data-page-number]');

        (async () => {
            for (let i = 0; i < pages.length; i++) {
                pages[i].scrollIntoView({ behavior: "instant", block: "center" });
                await new Promise(res => setTimeout(res, 300));

                let canvas = await html2canvas(pages[i], { scale: 1, useCORS: true });
                let dataUrl = canvas.toDataURL("image/jpeg", 0.7);

                if (i > 0) pdf.addPage();
                pdf.addImage(dataUrl, "JPEG", 0, 0, 595, 842);
                console.log(`✅ Captured page ${i + 1}`);
            }
            pdf.save("book.pdf");
        })();
    };
    document.body.appendChild(s2);
};
document.body.appendChild(s);
