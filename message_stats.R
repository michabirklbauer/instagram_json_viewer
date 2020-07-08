#!/usr/bin/env Rscript

# INSTAGRAM JSON VIEWER - Message Statistics
# 2020 (c) Micha Johannes Birklbauer
# https://github.com/t0xic-m/
# micha.birklbauer@gmail.com

library(ggplot2)

df = read.csv2("message_stats.csv", sep = ",", dec = ".")

ggplot(df, aes(x=reorder(conversation, -messages), y=messages)) + 
  geom_bar(stat="identity", color="black", fill="dodgerblue3", width = 0.7) + 
  ggtitle("Number of Messages per Contact") + 
  xlab("Conversation Partner (Instagram Username)") + 
  ylab("Number of Messages") + 
  geom_text(aes(label=messages), vjust=-0.3, size=3.0) + theme_minimal() + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

ggsave("message_stats.png")
ggsave("message_stats.jpeg")