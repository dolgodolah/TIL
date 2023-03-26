package com.example.kafka.controller

import com.example.kafka.dto.UserDTO
import com.example.kafka.service.KafkaProducerService
import org.springframework.web.bind.annotation.RestController
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody

@RestController
class KafkaController(
    private val kafkaProducerService: KafkaProducerService
) {

    @PostMapping("/send")
    fun sendMessage(@RequestBody user: UserDTO) {
        kafkaProducerService.sendMessage(user)
    }
}