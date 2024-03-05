<?php

require 'vendor/autoload.php';

use Dompdf\Dompdf;

// Load your Markdown content
$markdownContent = file_get_contents('index.md');

$emojiToRemove = ["👨‍💻", "🎓️", "🚀", "🇷🇺", "🇺🇸", "🌐", "💻️", "🏊‍♂️", "🏄‍♂️"]; // List emojis you want to remove
foreach ($emojiToRemove as $emoji) {
    $markdownContent = str_replace($emoji, '', $markdownContent); // Remove the emoji
}

// Convert Markdown with Twemoji images to HTML
$htmlContent = Parsedown::instance()->text($markdownContent);

$dompdf = new Dompdf();
$dompdf->loadHtml($htmlContent);
$dompdf->setPaper('A4', 'portrait');
$dompdf->render();

// Save the PDF
file_put_contents('butriman_cv.pdf', $dompdf->output());

