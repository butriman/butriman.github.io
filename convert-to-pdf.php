<?php

require 'vendor/autoload.php';

use Astrotomic\Twemoji\Twemoji;
use Dompdf\Dompdf;

// Load your Markdown content
$markdownContent = file_get_contents('index.md');

// Convert emojis to Twemoji image Markdown
$markdownContent = Twemoji::text($markdownContent)->toMarkdown();

// Convert Markdown with Twemoji images to HTML
$htmlContent = Parsedown::instance()->text($markdownContent);

$dompdf = new Dompdf();
$dompdf->loadHtml($htmlContent);
$dompdf->setPaper('A4', 'portrait');
$dompdf->render();

// Save the PDF
file_put_contents('butriman_cv.pdf', $dompdf->output());

