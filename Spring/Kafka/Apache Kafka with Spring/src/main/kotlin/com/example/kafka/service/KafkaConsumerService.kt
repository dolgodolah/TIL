package com.example.kafka.service

import org.springframework.kafka.annotation.KafkaListener
import org.springframework.stereotype.Service

@Service
class KafkaConsumerService {

    @KafkaListener(topics = ["example"], groupId = "test-consumer-group")
    fun listenGroupExample(message: String) {
        println("receive message : $message")
    }
}