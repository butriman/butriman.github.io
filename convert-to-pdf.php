<?php

require_once 'vendor/autoload.php';
include('path/to/emoji.php'); // Adjust the path as necessary

// Load your Markdown content
$markdownContent = file_get_contents('index.md');

// Convert Markdown to HTML
$htmlContent = Parsedown::instance()->text($markdownContent);

// Convert emojis to HTML
$htmlContent = emoji_unified_to_html($htmlContent);

use Dompdf\Dompdf;

$dompdf = new Dompdf();
$dompdf->loadHtml($htmlContent);
$dompdf->setPaper('A4', 'portrait');
$dompdf->render();

// Save the PDF
file_put_contents('butriman_cv.pdf', $dompdf->output());
